from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton

class AddEmployeeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Employee")

        self.name_input = QLineEdit()
        self.address_input = QLineEdit()
        self.city_input = QLineEdit()
        self.state_input = QLineEdit()
        self.zipcode_input = QLineEdit()
        self.num_witholdings_input = QLineEdit()
        self.salary_input = QLineEdit()
        self.num_dependents_input = QLineEdit()
        self.filing_status_input = QLineEdit()

        layout = QFormLayout()
        layout.addRow("Name:", self.name_input)
        layout.addRow("Address:", self.address_input)
        layout.addRow("City:", self.city_input)
        layout.addRow("State:", self.state_input)
        layout.addRow("Zip Code:", self.zipcode_input)
        layout.addRow("Number of Witholdings:", self.num_witholdings_input)
        layout.addRow("Salary:", self.salary_input)
        layout.addRow("Number of Dependents:", self.num_dependents_input)
        layout.addRow("Filing Status:", self.filing_status_input)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.accept)  # not save_employee
        layout.addWidget(save_button)

        self.setLayout(layout)

    def get_employee_data(self):
        return (self.name_input.text(), self.address_input.text(),
                 self.city_input.text(), self.state_input.text(), self.zipcode_input.text(),
                 self.num_witholdings_input.text(), self.salary_input.text(),
                 self.num_dependents_input.text(), self.filing_status_input.text())
        
