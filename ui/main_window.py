import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from ui.add_employee_dialog import AddEmployeeDialog
from ui.employee_table import EmployeeTableWidget
from models.employee_manager import EmployeeManager
from models.employee import Employee
from ui.add_customer_dialog import AddCustomerDialog
from ui.customer_table import CustomerTableWidget
from models.customer_manager import CustomerManager
from models.customer import Customer
from ui.add_vendor_dialog import AddVendorDialog
from ui.vendor_table import VendorTableWidget
from models.vendor_manager import VendorManager
from models.vendor import Vendor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Business Manager")

        self.employee_manager = EmployeeManager()
        self.customer_manager = CustomerManager()
        self.vendor_manager = VendorManager()

        layout = QVBoxLayout()
        open_employee_manager_btn = QPushButton("Employee Manager")
        open_employee_manager_btn.clicked.connect(self.open_employee_manager)
        layout.addWidget(open_employee_manager_btn)

        open_customer_manager_btn = QPushButton("Customer Manager")
        open_customer_manager_btn.clicked.connect(self.open_customer_manager)
        layout.addWidget(open_customer_manager_btn)

        open_vendor_manager_btn = QPushButton("Vendor Manager")
        open_vendor_manager_btn.clicked.connect(self.open_vendor_manager)
        layout.addWidget(open_vendor_manager_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_employee_manager(self):
        manager = EmployeeManager()
        self.employee_window = EmployeeTableWidget(manager)
        self.employee_window.show()

    def open_customer_manager(self):
        manager = CustomerManager()
        self.employee_window = CustomerTableWidget(manager)
        self.employee_window.show()

    def open_vendor_manager(self):
        manager = VendorManager()
        self.employee_window = VendorTableWidget(manager)
        self.employee_window.show()
        