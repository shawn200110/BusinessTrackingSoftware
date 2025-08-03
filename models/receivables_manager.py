import json
import datetime

class ReceivablesManager:
    def __init__(self, cash_manager,receivables_file="receivables.json"):
        self.cash_manager = cash_manager
        self.receivables_file = receivables_file
        self.receivables = []
        self.load_receivables()

    def add_receivable(self, customer, product, quantity, amount, due_date):
        receivable = {
            "customer": customer,
            "product": product,
            "quantity": quantity,
            "amount": amount,
            "due_date": due_date.isoformat(),
            "paid": False,
            "timestamp": datetime.datetime.now().isoformat()
        }
        self.receivables.append(receivable)
        self.save_receivables()

    def mark_as_paid(self, index):
        if 0 <= index < len(self.receivables):
            self.receivables[index]["paid"] = True
            self.receivables[index]["paid_timestamp"] = datetime.datetime.now().isoformat()
            self.save_receivables()

    def get_all_unpaid(self):
        return [r for r in self.receivables if not r["paid"]]

    def collect_receivables(self):
        today = datetime.date.today()
        for i, r in enumerate(self.receivables):
            due_date = datetime.date.fromisoformat(r["due_date"])
            if not r["paid"] and due_date <= today:
                self.cash_manager.add_transaction(
                    description=f"Collected receivable from {r['customer']}",
                    amount=r["amount"],
                    transaction_type="invoice"
                )
                self.receivables[i]["paid"] = True
                self.receivables[i]["paid_timestamp"] = datetime.datetime.now().isoformat()

        self.save_receivables()

    def save_receivables(self):
        with open(self.receivables_file, "w") as f:
            json.dump(self.receivables, f, indent=2)

    def load_receivables(self):
        try:
            with open(self.receivables_file, "r") as f:
                self.receivables = json.load(f)
        except FileNotFoundError:
            self.receivables = []