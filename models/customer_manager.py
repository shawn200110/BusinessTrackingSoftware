import json
from models.customer import Customer
from datetime import date
from dateutil.relativedelta import relativedelta

class CustomerManager:
    def __init__(self, cash_manager,receivables_manager,inventory_manager, data_file="customer.json"):
        self.receivables_manager = receivables_manager
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

    def process_sale(self, product_name: str, num_units: int, pm, im):
        product = pm.get_product_by_name(product_name)
        if not product:
            print("Product not found!")
            return

        if not product.is_physical:
            # no inventory change for digital goods
            return

        for component in product.bom:
            part_name = component["name"]
            required_qty = component["quantity"] * num_units
            im.remove_quantity(part_name, required_qty)

    def create_invoice(self, company_name):
        from ui.invoice_dialog import InvoiceDialog
        from models.product_manager import ProductManager
        from models.inventory_manager import InventoryManager
        pm = ProductManager()
        im = InventoryManager()
        product_names = [pm.products[i].name for i in range(len(pm.products))]
        dialog = InvoiceDialog(product_names=product_names)
        if dialog.exec():
            product_name,quantity = dialog.get_invoice_data()
        selected_product = pm.get_product_by_name(product_name)
        unit_price = selected_product.unit_price
        customer = [c for c in self.customer if c.company_name == company_name]
        customer = customer[0]
        im.verify_comfortable_quantities()
        self.process_sale(product_name, quantity, pm, im)
        due_date=date.today() + relativedelta(months=1)
        self.receivables_manager.add_receivable(
                                            customer=customer.company_name,
                                            product=product_name,
                                            quantity=quantity,
                                            amount=selected_product.unit_price,
                                            due_date=due_date
                                        )



        self.cash_manager.add_transaction(description=f"Invoice - {customer.company_name},{product_name},{str(quantity)}cnt", 
                                         amount=quantity*unit_price,
                                         transaction_type="invoice")
        print(f"Invoice for {customer.company_name} has been created.")
