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
from models.inventory_manager import InventoryManager
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(450, 200)
        self.setWindowTitle("Business Manager")
         
        self.cash_manager = CashManager() 
        self.inventory_manager = InventoryManager() 
        self.employee_manager = EmployeeManager(cash_manager=self.cash_manager)
        self.customer_manager = CustomerManager(cash_manager=self.cash_manager,
                                                inventory_manager=self.inventory_manager)
        self.vendor_manager = VendorManager(cash_manager=self.cash_manager,
                                            inventory_manager=self.inventory_manager)

        layout = QVBoxLayout()

        title_label = QLabel("Infinite Flow Music Company")
        title_font = QFont("Calibri", 24, QFont.Weight.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title_label)

        # Employee Manager Button 
        open_employee_manager_btn = QPushButton("Employee Manager")
        open_employee_manager_btn.setStyleSheet("""
                                QPushButton {
                                    background-color: #0078D7;
                                    color: white;
                                    font-size: 16px;
                                    padding: 8px 16px;
                                    border-radius: 6px;
                                }
                                QPushButton:hover {
                                    background-color: #005A9E;
                                }
                            """)
        open_employee_manager_btn.clicked.connect(self.open_employee_manager)
        layout.addWidget(open_employee_manager_btn)

        # Customer Manager Button
        open_customer_manager_btn = QPushButton("Customer Manager")
        open_customer_manager_btn.setStyleSheet("""
                                QPushButton {
                                    background-color: #B19CD9;
                                    color: white;
                                    font-size: 16px;
                                    padding: 8px 16px;
                                    border-radius: 6px;
                                }
                                QPushButton:hover {
                                    background-color: #6A0DAD;
                                }
                            """)
        open_customer_manager_btn.clicked.connect(self.open_customer_manager)
        layout.addWidget(open_customer_manager_btn)
        
        # Vendor Manager
        open_vendor_manager_btn = QPushButton("Vendor Manager")
        open_vendor_manager_btn.setStyleSheet("""
                                QPushButton {
                                    background-color: #A8D5BA;
                                    color: white;
                                    font-size: 16px;
                                    padding: 8px 16px;
                                    border-radius: 6px;
                                }
                                QPushButton:hover {
                                    background-color: #228B22;
                                }
                            """)
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
        