# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(645, 282)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(645, 282))
        palette = QPalette()
        brush = QBrush(QColor(236, 236, 236, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(204, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        brush3 = QBrush(QColor(240, 240, 240, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        Dialog.setPalette(palette)
        icon = QIcon()
        icon.addFile(u":/PrestoChangeO/images/magic-wand-64x64.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(0.900000000000000)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(250, 20, 381, 211))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 381, 51))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setIndent(0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 331, 141))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(True)
        self.imagelabel = QLabel(Dialog)
        self.imagelabel.setObjectName(u"imagelabel")
        self.imagelabel.setGeometry(QRect(28, 25, 201, 201))
        self.imagelabel.setFrameShape(QFrame.WinPanel)
        self.imagelabel.setFrameShadow(QFrame.Plain)
        self.imagelabel.setPixmap(QPixmap(u":/PrestoChangeO/images/GrandWarlock-256x256.png"))
        self.imagelabel.setScaledContents(True)
        self.imagelabel.setMargin(2)
        self.imagelabel.setIndent(3)
        self.OKButton = QPushButton(Dialog)
        self.OKButton.setObjectName(u"OKButton")
        self.OKButton.setGeometry(QRect(550, 250, 75, 24))
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-3, 230, 651, 20))
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"About Presto Change-O", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Presto Change-O", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>(c) 2022-present <a href=\"https://www.ryanboyd.io\"><span style=\" text-decoration: underline; color:#0000ff;\">Ryan L. Boyd</span></a></p><p>For more info/instructions, see<br> <a href=\"https://github.com/Red-Warlock/Presto-Change-O\"><span style=\" text-decoration: underline; color:#0000ff;\">github.com/Red-Warlock/Presto-Change-O</span></a></p><p>This software is open source and *completely free* to use.</p></body></html>", None))
        self.imagelabel.setText("")
        self.OKButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

