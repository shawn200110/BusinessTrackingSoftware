import json
from models.customer import Customer

class CustomerManager:
    def __init__(self, cash_manager, data_file="customer.json"):
        self.cash_manager = cash_manager
        self.data_file = data_file
        self.customer = []
        self.load_customers()

    def add_customer(self, customer: Customer):
        self.customer.append(customer)
        self.save_customer()

    def remove_customer(self, name: str):
        self.customer = [e for e in self.customer if e.company_name != name]
        self.save_customer()

    def save_customer(self):
        data = [{"company_name": e.company_name, "poc_name": e.poc_name, "address": e.address, "city": e.city, 
                 "state": e.state, "zipcode": e.zipcode} for e in self.customer]
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_customers(self):
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.customer = [Customer(**entry) for entry in data]
        except FileNotFoundError:
            self.customer = []