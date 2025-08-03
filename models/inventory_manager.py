# inventory_manager.py
import json
from dataclasses import dataclass
from typing import List
from PyQt6.QtWidgets import QMessageBox

@dataclass
class Inventory:
    name: str
    part_num: int
    cautious_quantity: int
    unit_price: float
    quantity: int = 0 
    

class InventoryManager:
    def __init__(self, data_file="inventory.json"):
        self.data_file = data_file
        self.items: List[Inventory] = []
        self.load()

    def load(self):
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.items = [Inventory(**entry) for entry in data]
        except FileNotFoundError:
            self.items = []

    def save(self):
        with open(self.data_file, "w") as f:
            json.dump([item.__dict__ for item in self.items], f, indent=2)

    def get_item_by_name(self, name: str) -> Inventory:
        for item in self.items:
            if item.name == name:
                return item
        return None
    
    def get_item_by_part_num(self, part_num: int) -> Inventory:
        for item in self.items:
            if item.part_num == part_num:
                return item
        return None

    def add_quantity(self, name: str, amount: int):
        item = self.get_item_by_name(name)
        if item:
            item.quantity += amount
            self.save()

    def remove_quantity(self, name: str, amount: int):
        item = self.get_item_by_name(name)
        if item:
            item.quantity = max(0, item.quantity - amount)
            self.save()

    def get_quantity(self, name: str) -> int:
        item = self.get_item_by_name(name)
        return item.quantity if item else 0

    def get_all_items(self) -> List[Inventory]:
        return self.items.copy()
    
    def verify_comfortable_quantities(self):
        for item in self.items:
            if item.quantity == 0:
                QMessageBox.warning(None,
                                    "Warning",
                                    "Not enough inventory to ship",
                                    QMessageBox.StandardButton.Ok
                                    )
                return 1
            if item.quantity < item.cautious_quantity:
                QMessageBox.warning(None,
                                    "Warning",
                                    f"You are running low on {item.name}, {item.part_num}\nCurrent Quantity: {item.quantity}",
                                    QMessageBox.StandardButton.Ok
                                    )
        return None

