from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox, QDateEdit
from PyQt6.QtCore import QDate

class DateRangeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Select Date Range")

        self.start_date_edit = QDateEdit(calendarPopup=True)
        self.start_date_edit.setDate(QDate.currentDate().addMonths(-1))  # Default: 1 month ago

        self.end_date_edit = QDateEdit(calendarPopup=True)
        self.end_date_edit.setDate(QDate.currentDate())

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Start Date:"))
        layout.addWidget(self.start_date_edit)
        layout.addWidget(QLabel("End Date:"))
        layout.addWidget(self.end_date_edit)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)

    def get_dates(self):
        return self.start_date_edit.date().toPyDate(), self.end_date_edit.date().toPyDate()