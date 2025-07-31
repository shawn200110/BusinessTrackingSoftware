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
from models.cash_manager import CashManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 200)
        self.setWindowTitle("Business Manager")
         
        self.cash_manager = CashManager() 
        self.employee_manager = EmployeeManager(cash_manager=self.cash_manager)
        self.customer_manager = CustomerManager(cash_manager=self.cash_manager)
        self.vendor_manager = VendorManager(cash_manager=self.cash_manager)

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
        # manager = EmployeeManager(cash_manager=self.cash_manager)
        manager = self.employee_manager
        self.employee_window = EmployeeTableWidget(manager)
        self.employee_window.show()

    def open_customer_manager(self):
        # manager = CustomerManager(cash_manager=self.cash_manager)
        manager = self.customer_manager
        self.customer_window = CustomerTableWidget(manager)
        self.customer_window.show()

    def open_vendor_manager(self):
        # manager = VendorManager(cash_manager=self.cash_manager)
        manager = self.vendor_manager
        self.vendor_window = VendorTableWidget(manager)
        self.vendor_window.show()
        