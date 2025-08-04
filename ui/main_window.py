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
from models.receivables_manager import ReceivablesManager
from models.inventory_manager import InventoryManager
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from ui.inventory_table import InventoryTableWidget 
from ui.add_expense_dialog import AddExpenseDialog



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(450, 450)
        self.setWindowTitle("Business Manager")
         
        self.cash_manager = CashManager() 
        self.receivables_manager = ReceivablesManager(cash_manager=self.cash_manager) 
        self.receivables_manager.collect_receivables()
        self.inventory_manager = InventoryManager() 
        self.employee_manager = EmployeeManager(cash_manager=self.cash_manager)
        self.customer_manager = CustomerManager(cash_manager=self.cash_manager,
                                                receivables_manager=self.receivables_manager,
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
                                    background-color: #d3d3d3;
                                    color: black;
                                    font-size: 16px;
                                    padding: 8px 16px;
                                    border-radius: 6px;
                                }
                                QPushButton:hover {
                                    background-color: #4f4f4f;
                                }
                            """)
        open_employee_manager_btn.clicked.connect(self.open_employee_manager)
        layout.addWidget(open_employee_manager_btn)

        # Customer Manager Button
        open_customer_manager_btn = QPushButton("Customer Manager")
        open_customer_manager_btn.setStyleSheet("""
                                QPushButton {
                                    background-color: #B19CD9;
                                    color: black;
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
                                    color: black;
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

        # View Inventory
        view_inventory_btn = QPushButton("View Inventory")
        view_inventory_btn.setStyleSheet("""
                                QPushButton {
                                    background-color: #FFF9C4;
                                    color: black;
                                    font-size: 16px;
                                    padding: 8px 16px;
                                    border-radius: 6px;
                                }
                                QPushButton:hover {
                                    background-color: #FFD700;
                                }
                            """)
        view_inventory_btn.clicked.connect(self.view_inventory)
        layout.addWidget(view_inventory_btn)

        # Add Expense
        add_expense_btn = QPushButton("Add General Expense")
        add_expense_btn.setStyleSheet("""
                                QPushButton {
                                    background-color: #FF6F61;
                                    color: black;
                                    font-size: 16px;
                                    padding: 8px 16px;
                                    border-radius: 6px;
                                }
                                QPushButton:hover {
                                    background-color: #8B0000;
                                }
                            """)
        add_expense_btn.clicked.connect(self.add_general_expense)
        layout.addWidget(add_expense_btn)

        # View Balance Sheet
        view_bal_sheet_btn = QPushButton("View Balance Sheet")
        view_bal_sheet_btn.setStyleSheet("""
                                QPushButton {
                                    background-color: #FFA726;
                                    color: black;
                                    font-size: 16px;
                                    padding: 8px 16px;
                                    border-radius: 6px;
                                }
                                QPushButton:hover {
                                    background-color: #EF6C00;
                                }
                            """)
        view_bal_sheet_btn.clicked.connect(self.show_balance_sheet)
        layout.addWidget(view_bal_sheet_btn)

        # View Income Statement
        view_income_statement_btn = QPushButton("View Income Statement")
        view_income_statement_btn.setStyleSheet("""
                                QPushButton {
                                    background-color: #C19A6B;
                                    color: black;
                                    font-size: 16px;
                                    padding: 8px 16px;
                                    border-radius: 6px;
                                }
                                QPushButton:hover {
                                    background-color: #5C4033;
                                }
                            """)
        view_income_statement_btn.clicked.connect(self.show_income_statement)
        layout.addWidget(view_income_statement_btn)

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

    def view_inventory(self):
        inventory_window = InventoryTableWidget(self.inventory_manager)
        inventory_window.show()
        inventory_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)  # optional
        self.inventory_popup = inventory_window  # keep a reference so it doesn't close

    def add_general_expense(self):
        dialog = AddExpenseDialog()
        if dialog.exec():
            data = dialog.get_data()
            self.cash_manager.add_transaction(
                description=data["description"] or f"Expense - {data['category']}",
                amount=-data["amount"],
                transaction_type="expense",
                expense_info=data
            )

    def show_balance_sheet(self):
        from ui.balance_sheet import BalanceSheetWindow

        data = self.generate_balance_sheet(self.cash_manager, self.inventory_manager, self.receivables_manager)
        self.balance_sheet_window = BalanceSheetWindow(data)
        self.balance_sheet_window.show()

    def generate_balance_sheet(self, cash_manager, inventory_manager, receivables_manager):
        # Assets
        cash = round(cash_manager.get_balance(), 2)
        receivables = round(sum([r["amount"] for r in receivables_manager.receivables]), 2)
        inventory = round(sum([i.quantity * i.unit_price for i in inventory_manager.items]), 2)
        
        total_current_assets = cash + receivables + inventory
        total_fixed_assets = 0  # Update if you add fixed assets like equipment, property, etc.
        total_assets = total_current_assets + total_fixed_assets

        # Liabilities (placeholders for now)
        short_term_liabilities = 0.00  # e.g., accounts payable, wages payable
        long_term_liabilities = 0.00   # e.g., loans payable
        total_liabilities = short_term_liabilities + long_term_liabilities

        # Equity
        net_worth = total_assets - total_liabilities

        return {
            # Assets
            "Cash": cash,
            "Accounts Receivable": receivables,
            "Inventory": inventory,
            "Total Current Assets": total_current_assets,
            "Total Fixed Assets": total_fixed_assets,
            "Total Assets": total_assets,

            # Liabilities
            "Short-Term Liabilities": short_term_liabilities,
            "Long-Term Liabilities": long_term_liabilities,
            "Total Liabilities": total_liabilities,

            # Equity
            "Net Worth": net_worth
        }
    
    def show_income_statement(self):
        from ui.income_statement import IncomeStatementWindow
        from ui.date_range_dialog import DateRangeDialog

        dialog = DateRangeDialog()
        if dialog.exec():
            start_date, end_date = dialog.get_dates()

        data = self.generate_income_statement(self.cash_manager,start_date,end_date)
        self.balance_sheet_window = IncomeStatementWindow(data,start_date,end_date)
        self.balance_sheet_window.show()
    
    
    def generate_income_statement(self,cash_manager, start, end):
        from datetime import date

        revenues = 0.0
        cogs = 0.0
        payroll = 0.0
        payroll_withholding = 0.0
        other_expenses = 0.0

        for tx in cash_manager.transactions:
            tx_time = date.fromisoformat(tx["timestamp"][:10])
            if start <= tx_time <= end:
                t_type = tx["type"]
                amount = tx["amount"]

                if t_type == "invoice":
                    revenues += amount
                    cogs += 0.3 * amount  # Assume COGS is 30% of sales
                elif t_type == "payroll":
                    payroll += abs(tx.get("gross_salary", amount))
                    payroll_withholding += sum([
                        abs(tx.get("federal_tax", 0)),
                        abs(tx.get("state_tax", 0)),
                        abs(tx.get("social_security_tax", 0)),
                        abs(tx.get("medicare_tax", 0))
                    ])
                elif t_type == "expense":
                    other_expenses += abs(amount)

        gross_profit = revenues - cogs
        total_expenses = payroll + payroll_withholding + other_expenses
        operating_income = gross_profit - total_expenses
        income_taxes = 0.2 * operating_income if operating_income > 0 else 0
        net_income = operating_income - income_taxes

        return {
            "Revenues": round(revenues, 2),
            "COGS": round(cogs, 2),
            "Gross Profit": round(gross_profit, 2),
            "Payroll": round(payroll, 2),
            "Payroll Withholding": round(payroll_withholding, 2),
            "Other Expenses": round(other_expenses, 2),
            "Total Expenses": round(total_expenses, 2),
            "Operating Income": round(operating_income, 2),
            "Income Taxes": round(income_taxes, 2),
            "Net Income": round(net_income, 2)
        }
        