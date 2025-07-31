from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout

class EmployeeTableWidget(QWidget):
    def __init__(self, employee_manager):
        super().__init__()
        self.employee_manager = employee_manager
        self.setFixedSize(900, 500)
        self.setWindowTitle("Employees")

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["Name", "Address","City","State", "Zip Code", "Witholdings", "Salary"])
        self.load_employees()

        add_button = QPushButton("Add Employee")
        add_button.clicked.connect(self.add_employee_dialog)

        delete_button = QPushButton("Remove Selected")
        delete_button.clicked.connect(self.remove_selected_employee)

        buttons = QHBoxLayout()
        buttons.addWidget(add_button)
        buttons.addWidget(delete_button)

        layout = QVBoxLayout()
        layout.addLayout(buttons)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def load_employees(self):
        self.table.setRowCount(0)
        for employee in self.employee_manager.employees:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(employee.name))
            self.table.setItem(row, 1, QTableWidgetItem(employee.address))
            self.table.setItem(row, 2, QTableWidgetItem(employee.city))
            self.table.setItem(row, 3, QTableWidgetItem(employee.state))
            self.table.setItem(row, 4, QTableWidgetItem(employee.zipcode))
            self.table.setItem(row, 5, QTableWidgetItem(f"{employee.num_witholdings:.2f}"))
            self.table.setItem(row, 6, QTableWidgetItem(f"{employee.salary:.2f}"))

    def add_employee_dialog(self):
        from ui.add_employee_dialog import AddEmployeeDialog
        from models.employee import Employee

        dialog = AddEmployeeDialog()
        if dialog.exec():
            name,address,city,state,zipcode,num_witholdings,salary = dialog.get_employee_data()
            try:
                num_witholdings = float(num_witholdings)
                salary = float(salary)
                employee = Employee(name=name,address=address,
                                    city=city,salary=salary,
                                    state=state,zipcode=zipcode,
                                    num_witholdings=num_witholdings)
                self.employee_manager.add_employee(employee)
                self.load_employees()
            except ValueError:
                print("Invalid data type.")

    def remove_selected_employee(self):
        selected = self.table.currentRow()
        if selected >= 0:
            name_item = self.table.item(selected, 0)
            if name_item:
                name = name_item.text()
                self.employee_manager.remove_employee(name)
                self.load_employees()