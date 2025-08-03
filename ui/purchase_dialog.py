from PyQt6.QtWidgets import QDialog, QFormLayout, QComboBox, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox

class PurchaseDialog(QDialog):
    def __init__(self, product_names):
        super().__init__()
        self.setWindowTitle("Purchase Inventory")
        self.setMinimumSize(300, 150)

        self.quantity_input = QLineEdit()
        self.quantity_input.setPlaceholderText("Enter quantity")

        self.status_label = QLabel()

        form_layout = QFormLayout()
        form_layout.addRow("Product:", self.product_dropdown)
        form_layout.addRow("Quantity:", self.quantity_input)

        submit_btn = QPushButton("Create Invoice")
        submit_btn.clicked.connect(self.validate_and_accept)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(submit_btn)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def validate_and_accept(self):
        try:
            quantity = int(self.quantity_input.text())
            if quantity <= 0:
                raise ValueError
            self.accept()
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid quantity.")

    def get_invoice_data(self):
        product_name = self.product_dropdown.currentText()
        quantity = int(self.quantity_input.text())
        return product_name, quantity