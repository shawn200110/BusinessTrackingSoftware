from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton

class AddVendorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Vendor")

        self.name_input = QLineEdit()
        self.part_num_input = QLineEdit()
        self.unit_price_input = QLineEdit()
        self.address_input = QLineEdit()
        self.city_input = QLineEdit()
        self.state_input = QLineEdit()
        self.zipcode_input = QLineEdit()

        layout = QFormLayout()
        layout.addRow("Vendor Name:", self.name_input)
        layout.addRow("Part Number:", self.part_num_input)
        layout.addRow("Unit Price", self.unit_price_input)
        layout.addRow("Address:", self.address_input)
        layout.addRow("City:", self.city_input)
        layout.addRow("State:", self.state_input)
        layout.addRow("Zip Code:", self.zipcode_input)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.accept)  # not save_employee
        layout.addWidget(save_button)

        self.setLayout(layout)

    def get_vendor_data(self):
        return (self.name_input.text(),self.part_num_input.text(), self.unit_price_input.text(),
                 self.address_input.text(),self.city_input.text(),
                   self.state_input.text(), self.zipcode_input.text())