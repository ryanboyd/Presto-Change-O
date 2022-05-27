from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
import resources_rc


class MessageBoxShower():

    appId = None

    def __init__(self, appId: str):
        # Set up the universal icon for this app
        self.appId = appId

    def ShowErrorMessageBox(self, error_msg: str) -> None:
        appIcon = QIcon()
        appIcon.addFile(u":/PrestoChangeO/images/magic-wand-64x64.png", QSize(), QIcon.Normal, QIcon.Off)

        msgBox = QMessageBox()
        msgBox.setWindowTitle(f"{self.appId}: Error")
        msgBox.setWindowIcon(appIcon)
        msgBox.setText(error_msg)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setIcon(QMessageBox.Critical)
        ret = msgBox.exec()

        return

    def ShowInformationMessageBox(self, info_msg: str) -> None:
        appIcon = QIcon()
        appIcon.addFile(u":/PrestoChangeO/images/magic-wand-64x64.png", QSize(), QIcon.Normal, QIcon.Off)

        msgBox = QMessageBox()
        msgBox.setWindowTitle(f"{self.appId}: Information")
        msgBox.setWindowIcon(appIcon)
        msgBox.setText(info_msg)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setIcon(QMessageBox.Information)
        ret = msgBox.exec()