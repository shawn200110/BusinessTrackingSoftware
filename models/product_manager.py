import json

class Product:
    def __init__(self, name, unit_price, is_physical=False, bom=None):
        self.name = name
        self.unit_price = unit_price
        self.is_physical = is_physical
        self.bom = bom or []

class ProductManager:
    def __init__(self, file="products.json"):
        self.file = file
        self.products = []
        self.load_products()

    def load_products(self):
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
                self.products = [Product(**item) for item in data]
        except FileNotFoundError:
            self.products = []

    def get_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None



    