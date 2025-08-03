from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

class InventoryTableWidget(QWidget):
    def __init__(self, inventory_manager):
        super().__init__()
        self.setWindowTitle("Inventory")
        self.resize(400, 300)

        layout = QVBoxLayout()
        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.setLayout(layout)

        self.inventory_manager = inventory_manager
        self.populate_table()

    def populate_table(self):
        items = self.inventory_manager.get_all_items()
        self.table.setRowCount(len(items))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Part Number", "Quantity"])

        for row, item in enumerate(items):
            self.table.setItem(row, 0, QTableWidgetItem(item.name))
            self.table.setItem(row, 1, QTableWidgetItem(str(item.part_num)))
            self.table.setItem(row, 2, QTableWidgetItem(str(item.quantity)))