from qt6_forms.about_dialog import Ui_Dialog
from PySide6.QtWidgets import QDialog
import resources_rc

class AboutDialog(QDialog):
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.OKButton.clicked.connect(self.close)

def ShowAbout():
    aboutDialog = AboutDialog()
    aboutDialog.exec()
    return