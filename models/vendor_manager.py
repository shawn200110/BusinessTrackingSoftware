import json
from models.vendor import Vendor

class VendorManager:
    def __init__(self, data_file="vendor.json"):
        self.data_file = data_file
        self.vendor = []
        self.load_vendor()

    def add_vendor(self, vendor: Vendor):
        self.vendor.append(vendor)
        self.save_vendor()

    def remove_vendor(self, name: str):
        self.vendor = [e for e in self.vendor if e.name != name]
        self.save_vendor()


    def save_vendor(self):
        data = [{"company name": e.name, "part_num": e.part_num, "unit_price": e.unit_price, "address": e.address, "city": e.city, 
                 "state": e.state, "zipcode": e.zipcode} for e in self.vendor]
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_vendor(self):
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.vendor = [Vendor(**entry) for entry in data]
        except FileNotFoundError:
            self.vendor = []