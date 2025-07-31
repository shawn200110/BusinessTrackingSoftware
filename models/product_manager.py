from dataclasses import dataclass

@dataclass
class Product:
    def __init__(self, name, unit_price, bom=None, is_physical=False):
        self.name = name
        self.unit_price = unit_price
        self.is_physical = is_physical
        self.bom = bom or []  # List of (component_name, quantity)



    