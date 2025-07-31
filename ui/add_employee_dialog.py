from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton

class AddEmployeeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Employee")

        self.name_input = QLineEdit()
        self.salary_input = QLineEdit()

        layout = QFormLayout()
        layout.addRow("Name:", self.name_input)
        layout.addRow("Salary:", self.salary_input)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.accept)  # not save_employee
        layout.addWidget(save_button)

        self.setLayout(layout)

    def get_employee_data(self):
        return self.name_input.text(), self.salary_input.text()
