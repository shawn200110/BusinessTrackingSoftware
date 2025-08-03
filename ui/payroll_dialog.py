from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel
import json

class PayrollHistoryDialog(QDialog):
    def __init__(self, cash_file="cash.json"):
        super().__init__()
        self.setWindowTitle("Payroll History")
        self.resize(800, 400)

        layout = QVBoxLayout()
        self.table = QTableWidget()
        layout.addWidget(QLabel("Payroll Events:"))
        layout.addWidget(self.table)
        self.setLayout(layout)

        self.load_payroll_data(cash_file)

    def load_payroll_data(self, cash_file):
        try:
            with open(cash_file, "r") as f:
                data = json.load(f)
                transactions = data.get("transactions", [])
        except FileNotFoundError:
            transactions = []

        payroll_events = [t for t in transactions if t.get("type") == "payroll"]

        headers = [
            "Description", "Gross Salary", "Federal Tax", "State Tax",
            "Social Security", "Medicare", "Net Paid", "Timestamp"
        ]

        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setRowCount(len(payroll_events))

        for row, event in enumerate(payroll_events):
            self.table.setItem(row, 0, QTableWidgetItem(event.get("description", "")))
            self.table.setItem(row, 1, QTableWidgetItem(f"${event.get('gross_salary', 0):,.2f}"))
            self.table.setItem(row, 2, QTableWidgetItem(f"${event.get('federal_tax', 0):,.2f}"))
            self.table.setItem(row, 3, QTableWidgetItem(f"${event.get('state_tax', 0):,.2f}"))
            self.table.setItem(row, 4, QTableWidgetItem(f"${event.get('social_security_tax', 0):,.2f}"))
            self.table.setItem(row, 5, QTableWidgetItem(f"${event.get('medicare_tax', 0):,.2f}"))
            self.table.setItem(row, 6, QTableWidgetItem(f"${event.get('net_paid', 0):,.2f}"))
            self.table.setItem(row, 7, QTableWidgetItem(event.get("timestamp", "")))