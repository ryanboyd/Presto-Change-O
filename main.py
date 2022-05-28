import sys
from config import Config, init_app_id
from MainWindow import MainWindow

from PySide6.QtWidgets import QApplication





if __name__ == "__main__":

    #tell windows that this is not just pythonw
    init_app_id()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())