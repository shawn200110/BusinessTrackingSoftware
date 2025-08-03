from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class BalanceSheetWindow(QWidget):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("Balance Sheet")
        self.setGeometry(200, 200, 400, 450)

        layout = QVBoxLayout()

        # Assets section
        layout.addWidget(QLabel("<b>Assets</b>"))
        layout.addWidget(QLabel(f"Cash: ${data['Cash']:.2f}"))
        layout.addWidget(QLabel(f"Accounts Receivable: ${data['Accounts Receivable']:.2f}"))
        layout.addWidget(QLabel(f"Inventory: ${data['Inventory']:.2f}"))
        layout.addWidget(QLabel(f"<b>Total Current Assets: ${data['Total Current Assets']:.2f}</b>"))
        layout.addWidget(QLabel(f"Total Fixed Assets: ${data['Total Fixed Assets']:.2f}"))
        layout.addWidget(QLabel(f"<b>Total Assets: ${data['Total Assets']:.2f}</b>"))

        layout.addSpacing(10)

        # Liabilities and Equity section
        layout.addWidget(QLabel("<b>Liabilities & Net Worth</b>"))
        layout.addWidget(QLabel(f"Short-Term Liabilities: ${data['Short-Term Liabilities']:.2f}"))
        layout.addWidget(QLabel(f"Long-Term Liabilities: ${data['Long-Term Liabilities']:.2f}"))
        layout.addWidget(QLabel(f"<b>Total Liabilities: ${data['Total Liabilities']:.2f}</b>"))
        layout.addWidget(QLabel(f"<b>Net Worth: ${data['Net Worth']:.2f}</b>"))

        self.setLayout(layout)