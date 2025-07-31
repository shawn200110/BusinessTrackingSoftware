import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from ui.add_employee_dialog import AddEmployeeDialog
from ui.employee_table import EmployeeTableWidget
from models.employee_manager import EmployeeManager
from models.employee import Employee

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Business Manager")

        self.employee_manager = EmployeeManager()

        layout = QVBoxLayout()
        open_employee_manager_btn = QPushButton("Employee Manager")
        open_employee_manager_btn.clicked.connect(self.open_employee_manager)
        layout.addWidget(open_employee_manager_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_employee_manager(self):
        manager = EmployeeManager()
        self.employee_window = EmployeeTableWidget(manager)
        self.employee_window.show()
        