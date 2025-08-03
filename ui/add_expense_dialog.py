from PyQt6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QComboBox, QLineEdit, QPushButton

class AddExpenseDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add General Expense")

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.amount_input = QLineEdit()
        self.category_dropdown = QComboBox()
        self.description_input = QLineEdit()

        # Add expense categories
        categories = [
            "Rent", "Utilities", "Insurance", "Office Supplies", "Marketing",
            "Legal and Professional Services", "Travel and Meals",
            "Maintenance and Repairs", "Subscriptions & Software", "Miscellaneous"
        ]
        self.category_dropdown.addItems(categories)

        form_layout.addRow("Amount:", self.amount_input)
        form_layout.addRow("Category:", self.category_dropdown)
        form_layout.addRow("Description:", self.description_input)

        layout.addLayout(form_layout)

        self.submit_btn = QPushButton("Add Expense")
        self.submit_btn.clicked.connect(self.accept)
        layout.addWidget(self.submit_btn)

        self.setLayout(layout)

    def get_data(self):
        return {
            "amount": float(self.amount_input.text()),
            "category": self.category_dropdown.currentText(),
            "description": self.description_input.text()
        }