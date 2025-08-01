import json
import datetime

class CashManager:
    def __init__(self, file_name="cash.json"):
        self.file_name = file_name
        self.balance = 200000.00  # Initial investment
        self.transactions = []
        self.load()

    def add_transaction(self, description, amount, transaction_type):
        # amount: positive = cash in, negative = cash out
        self.balance += amount
        transaction = {
            "description": description,
            "amount": amount,
            "type": transaction_type,
            "balance_after": self.balance,
            "timestamp": datetime.datetime.now().isoformat()
        }
        self.transactions.append(transaction)
        self.save()

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