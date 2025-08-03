import json
from models.vendor import Vendor

class VendorManager:
    def __init__(self, cash_manager, inventory_manager, data_file="vendor.json"):
        self.cash_manager = cash_manager
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
        data = [{"vendor_name": e.vendor_name, "part_id": e.part_id, "part_num": e.part_num, "unit_price": e.unit_price, "address": e.address, "city": e.city, 
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

    def purchase_inventory(self,part_num,quantity):
        from ui.invoice_dialog import InvoiceDialog
        from models.product_manager import ProductManager
        from models.inventory_manager import InventoryManager
        im = InventoryManager()
        pm = ProductManager()
        item = im.get_item_by_part_num(part_num)
        im.add_quantity(item.name, quantity)
        vendor = [v for v in self.vendor if int(v.part_num) == part_num]
        vendor=vendor[0]
        unit_price = float(vendor.unit_price)
        
        self.cash_manager.add_transaction(description=f"Purchase - {vendor.vendor_name},{vendor.part_id},{part_num},{str(quantity)}cnt", 
                                         amount=-quantity*unit_price,
                                         transaction_type="purchase")
        print(f"Purchase for {item.name} has been created.")