from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem
import json

class InvoiceHistoryDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sales History")
        self.resize(800, 400)

        layout = QVBoxLayout()
        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.setLayout(layout)

        self.load_sales()

    def load_sales(self):
        with open("cash.json", "r") as f:
            data = json.load(f)
            transactions = data.get("transactions", [])
            sales = [t for t in transactions if t.get("type") == "invoice"]

        headers = ["Date", "Customer", "Product", "Qty", "Amount"]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setRowCount(len(sales))

        for row, t in enumerate(sales):
            # Parse format: "Invoice - Customer,Product,Qty"
            try:
                _, details = t["description"].split(" - ", 1)
                customer, product, qty = details.split(",")
            except ValueError:
                customer = product = qty = "N/A"

            self.table.setItem(row, 0, QTableWidgetItem(t.get("timestamp", "")[:10]))
            self.table.setItem(row, 1, QTableWidgetItem(customer))
            self.table.setItem(row, 2, QTableWidgetItem(product))
            self.table.setItem(row, 3, QTableWidgetItem(qty))
            self.table.setItem(row, 4, QTableWidgetItem(f"${t.get('amount', 0):.2f}"))