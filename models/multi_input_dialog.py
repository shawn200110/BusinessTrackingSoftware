from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton

class QuickMultiInputDialog(QDialog):
    def __init__(self, fields: list[str]):
        super().__init__()
        self.setWindowTitle("Enter Information")
        self.inputs = {}

        layout = QFormLayout()
        for field in fields:
            line = QLineEdit()
            self.inputs[field] = line
            layout.addRow(field + ":", line)

        save_btn = QPushButton("OK")
        save_btn.clicked.connect(self.accept)
        layout.addWidget(save_btn)
        self.setLayout(layout)

    def get_inputs(self):
        return {name: widget.text() for name, widget in self.inputs.items()}