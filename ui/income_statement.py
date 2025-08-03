from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class IncomeStatementWindow(QWidget):
    def __init__(self, data, start_date, end_date):
        super().__init__()
        self.setWindowTitle("Income Statement")
        self.setGeometry(250, 250, 400, 400)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"<b>Income Statement</b><br>Period: {start_date} to {end_date}"))

        layout.addSpacing(10)
        layout.addWidget(QLabel(f"Sales: ${data['Revenues']:.2f}"))
        layout.addWidget(QLabel(f"COGS: ${data['COGS']:.2f}"))
        layout.addWidget(QLabel(f"<b>Gross Profit: ${data['Gross Profit']:.2f}</b>"))

        layout.addSpacing(10)
        layout.addWidget(QLabel(f"<b>Expenses</b>"))
        layout.addWidget(QLabel(f"Payroll: ${data['Payroll']:.2f}"))
        layout.addWidget(QLabel(f"Payroll Withholding: ${data['Payroll Withholding']:.2f}"))
        layout.addWidget(QLabel(f"Other Expenses: ${data['Other Expenses']:.2f}"))
        layout.addWidget(QLabel(f"<b>Total Expenses: ${data['Total Expenses']:.2f}</b>"))

        layout.addSpacing(10)
        layout.addWidget(QLabel(f"Operating Income: ${data['Operating Income']:.2f}"))
        layout.addWidget(QLabel(f"Income Taxes: ${data['Income Taxes']:.2f}"))
        layout.addWidget(QLabel(f"<b>Net Income: ${data['Net Income']:.2f}</b>"))

        self.setLayout(layout)