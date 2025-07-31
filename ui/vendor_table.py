from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout

class VendorTableWidget(QWidget):
    def __init__(self, vendor_manager):
        super().__init__()
        self.vendor_manager = vendor_manager
        self.setFixedSize(900, 500)
        self.setWindowTitle("Vendors")

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["Name", "Address","City","State", "Zip Code", "Number of Witholdings", "Salary"])
        self.load_vendors()

        add_button = QPushButton("Add Vendor")
        add_button.clicked.connect(self.add_vendor_dialog)

        delete_button = QPushButton("Remove Selected")
        delete_button.clicked.connect(self.remove_selected_vendor)

        buttons = QHBoxLayout()
        buttons.addWidget(add_button)
        buttons.addWidget(delete_button)

        layout = QVBoxLayout()
        layout.addLayout(buttons)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def load_vendors(self):
        self.table.setRowCount(0)
        for vendor in self.vendor_manager.vendor:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(vendor.name))
            self.table.setItem(row, 1, QTableWidgetItem(vendor.part_num))
            self.table.setItem(row, 2, QTableWidgetItem(vendor.unit_price))
            self.table.setItem(row, 3, QTableWidgetItem(vendor.address))
            self.table.setItem(row, 4, QTableWidgetItem(vendor.city))
            self.table.setItem(row, 5, QTableWidgetItem(vendor.state))
            self.table.setItem(row, 6, QTableWidgetItem(vendor.zipcode))

    def add_vendor_dialog(self):
        from ui.add_vendor_dialog import AddVendorDialog
        from models.vendor import Vendor

        dialog = AddVendorDialog()
        if dialog.exec():
            name,part_num,unit_price,address,city,state,zipcode = dialog.get_vendor_data()
            try:
                vendor = Vendor(name=name,part_num=part_num,unit_price=unit_price,
                                address=address,city=city,
                                    state=state,zipcode=zipcode)
                self.vendor_manager.add_vendor(vendor)
                self.load_vendors()
            except ValueError:
                print("Invalid data type.")

    def remove_selected_vendor(self):
        selected = self.table.currentRow()
        if selected >= 0:
            name_item = self.table.item(selected, 0)
            if name_item:
                name = name_item.text()
                self.vendor_manager.remove_vendor(name)
                self.load_vendors()