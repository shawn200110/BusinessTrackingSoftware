import sys
# import os

# project_root = os.path.abspath(os.path.dirname(__file__))
# if project_root not in sys.path:
#     sys.path.insert(0, project_root)
    
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

