from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton

class AddCustomerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Customer")

        self.company_name_input = QLineEdit()
        self.poc_name_input = QLineEdit()
        self.address_input = QLineEdit()
        self.city_input = QLineEdit()
        self.state_input = QLineEdit()
        self.zipcode_input = QLineEdit()

        layout = QFormLayout()
        layout.addRow("Company Name:", self.company_name_input)
        layout.addRow("Point-of-Contact Name:", self.poc_name_input)
        layout.addRow("Address:", self.address_input)
        layout.addRow("City:", self.city_input)
        layout.addRow("State:", self.state_input)
        layout.addRow("Zip Code:", self.zipcode_input)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.accept)  # not save_employee
        layout.addWidget(save_button)

        self.setLayout(layout)

    def get_customer_data(self):
        return (self.company_name_input.text(),self.poc_name_input.text(),
                 self.address_input.text(),self.city_input.text(),
                   self.state_input.text(), self.zipcode_input.text())