from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout

class CustomerTableWidget(QWidget):
    def __init__(self, customer_manager):
        super().__init__()
        self.customer_manager = customer_manager
        self.setFixedSize(900, 500)
        self.setWindowTitle("Customers")

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["Name", "Address","City","State", "Zip Code", "Witholdings", "Salary"])
        self.load_customers()

        add_button = QPushButton("Add Customer")
        add_button.clicked.connect(self.add_customer_dialog)

        delete_button = QPushButton("Remove Selected")
        delete_button.clicked.connect(self.remove_selected_customer)

        buttons = QHBoxLayout()
        buttons.addWidget(add_button)
        buttons.addWidget(delete_button)

        layout = QVBoxLayout()
        layout.addLayout(buttons)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def load_customers(self):
        self.table.setRowCount(0)
        for customer in self.customer_manager.customer:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(customer.company_name))
            self.table.setItem(row, 1, QTableWidgetItem(customer.poc_name))
            self.table.setItem(row, 2, QTableWidgetItem(customer.address))
            self.table.setItem(row, 3, QTableWidgetItem(customer.city))
            self.table.setItem(row, 4, QTableWidgetItem(customer.state))
            self.table.setItem(row, 5, QTableWidgetItem(customer.zipcode))

    def add_customer_dialog(self):
        from ui.add_customer_dialog import AddCustomerDialog
        from models.customer import Customer

        dialog = AddCustomerDialog()
        if dialog.exec():
            company_name,poc_name,address,city,state,zipcode = dialog.get_customer_data()
            try:
                customer = Customer(company_name=company_name,poc_name=poc_name,
                                    address=address,city=city,
                                    state=state,zipcode=zipcode)
                self.customer_manager.add_customer(customer)
                self.load_customers()
            except ValueError:
                print("Invalid data type.")

    def remove_selected_customer(self):
        selected = self.table.currentRow()
        if selected >= 0:
            name_item = self.table.item(selected, 0)
            if name_item:
                name = name_item.text()
                self.customer_manager.remove_customer(name)
                self.load_customers()