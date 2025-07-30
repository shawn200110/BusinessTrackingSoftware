import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Business Manager")

        layout = QVBoxLayout()
        layout.addWidget(QPushButton("View Balance Sheet"))
        layout.addWidget(QPushButton("Add Employee"))
        layout.addWidget(QPushButton("Create Invoice"))
        layout.addWidget(QPushButton("Exit", clicked=self.close))

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

