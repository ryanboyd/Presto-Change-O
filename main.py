import sys

import config
from MainWindow import MainWindow

from PySide6.QtWidgets import QApplication


if __name__ == "__main__":

    #initialize all of the global stuff
    config.init()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())