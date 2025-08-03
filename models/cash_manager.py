import json
import datetime

class CashManager:
    def __init__(self, file_name="cash.json"):
        self.file_name = file_name
        self.balance = 200000.00  # Initial investment
        self.transactions = []
        self.load()

    def add_transaction(self, description, amount, transaction_type, payroll_info=None, expense_info=None):
        # amount: positive = cash in, negative = cash out
        self.balance += amount
        transaction = {
            "description": description,
            "amount": amount,
            "type": transaction_type,
            "balance_after": self.balance,
            "timestamp": datetime.datetime.now().isoformat()
        }

        if transaction_type == "payroll":
            transaction.update({
                "gross_salary": payroll_info.get("salary"),
                "federal_tax": payroll_info.get("federal_tax"),
                "state_tax": payroll_info.get("state_tax"),
                "social_security_tax": payroll_info.get("social_security_tax"),
                "medicare_tax": payroll_info.get("medicare_tax"),
                "net_paid": payroll_info.get("amount_paid")
            })
        elif transaction_type == "expense":
            transaction.update({
                "amount": expense_info.get("amount"),
                "category": expense_info.get("category"),
                "description": expense_info.get("description")
            })
        

        self.transactions.append(transaction)
        self.save()

    def get_balance(self):
        return self.balance

    def save(self):
        with open(self.file_name, "w") as f:
            json.dump({
                "balance": self.balance,
                "transactions": self.transactions
            }, f, indent=2)

    def load(self):
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
                self.balance = data["balance"]
                self.transactions = data["transactions"]
        except FileNotFoundError:
            self.balance = 200000.00
            self.transactions = []