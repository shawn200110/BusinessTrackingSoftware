from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem
import json

class PurchaseHistoryDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Purchase History")
        self.resize(800, 400)

        layout = QVBoxLayout()
        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.setLayout(layout)

        self.load_purchases()

    def load_purchases(self):
        with open("cash.json", "r") as f:
            data = json.load(f)
            transactions = data.get("transactions", [])
            purchases = [t for t in transactions if t.get("type") == "purchase"]

        headers = ["Date", "Vendor", "Item", "Part#", "Qty", "Amount"]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setRowCount(len(purchases))

        for row, t in enumerate(purchases):
            # Parse purchase description format: "Purchase - Vendor,Item,Part#,Qty"
            try:
                _, details = t["description"].split(" - ", 1)
                vendor, item, part_num, qty = details.split(",")
            except ValueError:
                vendor = item = part_num = qty = "N/A"

            self.table.setItem(row, 0, QTableWidgetItem(t.get("timestamp", "")[:10]))
            self.table.setItem(row, 1, QTableWidgetItem(vendor))
            self.table.setItem(row, 2, QTableWidgetItem(item))
            self.table.setItem(row, 3, QTableWidgetItem(part_num))
            self.table.setItem(row, 4, QTableWidgetItem(qty))
            self.table.setItem(row, 5, QTableWidgetItem(f"${abs(t.get('amount', 0)):.2f}"))