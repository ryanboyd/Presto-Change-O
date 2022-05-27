# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt6_mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(667, 638)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u":/PrestoChangeO/images/magic-wand-64x64.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 590, 621, 31))
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.StatusLabel = QLabel(self.centralwidget)
        self.StatusLabel.setObjectName(u"StatusLabel")
        self.StatusLabel.setGeometry(QRect(20, 550, 621, 31))
        self.StatusLabel.setAutoFillBackground(False)
        self.StatusLabel.setFrameShape(QFrame.Box)
        self.RunButton = QPushButton(self.centralwidget)
        self.RunButton.setObjectName(u"RunButton")
        self.RunButton.setGeometry(QRect(200, 430, 231, 61))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.RunButton.setFont(font)
        self.RunButton.setFocusPolicy(Qt.WheelFocus)
        self.folderChooserGroupbox = QGroupBox(self.centralwidget)
        self.folderChooserGroupbox.setObjectName(u"folderChooserGroupbox")
        self.folderChooserGroupbox.setGeometry(QRect(20, 20, 621, 221))
        font1 = QFont()
        font1.setPointSize(11)
        self.folderChooserGroupbox.setFont(font1)
        self.OutputFolderLineEdit = QLineEdit(self.folderChooserGroupbox)
        self.OutputFolderLineEdit.setObjectName(u"OutputFolderLineEdit")
        self.OutputFolderLineEdit.setEnabled(False)
        self.OutputFolderLineEdit.setGeometry(QRect(140, 140, 431, 41))
        font2 = QFont()
        font2.setPointSize(10)
        self.OutputFolderLineEdit.setFont(font2)
        self.ChooseOutputFolderButton = QPushButton(self.folderChooserGroupbox)
        self.ChooseOutputFolderButton.setObjectName(u"ChooseOutputFolderButton")
        self.ChooseOutputFolderButton.setGeometry(QRect(30, 130, 101, 61))
        self.ChooseOutputFolderButton.setFont(font2)
        self.ChooseOutputFolderButton.setFocusPolicy(Qt.WheelFocus)
        self.InputFolderLineEdit = QLineEdit(self.folderChooserGroupbox)
        self.InputFolderLineEdit.setObjectName(u"InputFolderLineEdit")
        self.InputFolderLineEdit.setEnabled(False)
        self.InputFolderLineEdit.setGeometry(QRect(140, 50, 431, 41))
        self.InputFolderLineEdit.setFont(font2)
        self.ChooseInputFolderButton = QPushButton(self.folderChooserGroupbox)
        self.ChooseInputFolderButton.setObjectName(u"ChooseInputFolderButton")
        self.ChooseInputFolderButton.setGeometry(QRect(30, 40, 101, 61))
        self.ChooseInputFolderButton.setFont(font2)
        self.ChooseInputFolderButton.setAutoDefault(False)
        self.ChooseInputFolderButton.setFlat(False)
        self.ExtraFileOptionsGroupbox = QGroupBox(self.centralwidget)
        self.ExtraFileOptionsGroupbox.setObjectName(u"ExtraFileOptionsGroupbox")
        self.ExtraFileOptionsGroupbox.setGeometry(QRect(20, 260, 621, 101))
        self.ExtraFileOptionsGroupbox.setFont(font1)
        self.IncludeNonAudioCheckbox = QCheckBox(self.ExtraFileOptionsGroupbox)
        self.IncludeNonAudioCheckbox.setObjectName(u"IncludeNonAudioCheckbox")
        self.IncludeNonAudioCheckbox.setGeometry(QRect(10, 40, 431, 31))
        self.IncludeNonAudioCheckbox.setChecked(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.folderChooserGroupbox.raise_()
        self.progressBar.raise_()
        self.StatusLabel.raise_()
        self.RunButton.raise_()
        self.ExtraFileOptionsGroupbox.raise_()

        self.retranslateUi(MainWindow)

        self.RunButton.setDefault(False)
        self.ChooseOutputFolderButton.setDefault(False)
        self.ChooseInputFolderButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Presto Change-O", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.StatusLabel.setText(QCoreApplication.translate("MainWindow", u"Waiting to process...", None))
        self.RunButton.setText(QCoreApplication.translate("MainWindow", u"Convert Files!", None))
        self.folderChooserGroupbox.setTitle(QCoreApplication.translate("MainWindow", u"Choose Input and Output Locations", None))
        self.ChooseOutputFolderButton.setText(QCoreApplication.translate("MainWindow", u"Choose\n"
"Output Folder", None))
        self.ChooseInputFolderButton.setText(QCoreApplication.translate("MainWindow", u"Choose \n"
"Input Folder", None))
        self.ExtraFileOptionsGroupbox.setTitle(QCoreApplication.translate("MainWindow", u"Extra File Options", None))
        self.IncludeNonAudioCheckbox.setText(QCoreApplication.translate("MainWindow", u"Copy Non-Audio Files to Output (e.g., images, log files, etc.)", None))
    # retranslateUi

