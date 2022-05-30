# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(672, 692)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u":/PrestoChangeO/images/magic-wand-64x64.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 640, 631, 31))
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.StatusLabel = QLabel(self.centralwidget)
        self.StatusLabel.setObjectName(u"StatusLabel")
        self.StatusLabel.setGeometry(QRect(20, 600, 631, 31))
        self.StatusLabel.setAutoFillBackground(False)
        self.StatusLabel.setFrameShape(QFrame.Box)
        self.RunButton = QPushButton(self.centralwidget)
        self.RunButton.setObjectName(u"RunButton")
        self.RunButton.setGeometry(QRect(70, 500, 231, 61))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.RunButton.setFont(font)
        self.RunButton.setFocusPolicy(Qt.WheelFocus)
        self.folderChooserGroupbox = QGroupBox(self.centralwidget)
        self.folderChooserGroupbox.setObjectName(u"folderChooserGroupbox")
        self.folderChooserGroupbox.setGeometry(QRect(20, 20, 631, 171))
        font1 = QFont()
        font1.setPointSize(11)
        self.folderChooserGroupbox.setFont(font1)
        self.OutputFolderLineEdit = QLineEdit(self.folderChooserGroupbox)
        self.OutputFolderLineEdit.setObjectName(u"OutputFolderLineEdit")
        self.OutputFolderLineEdit.setEnabled(False)
        self.OutputFolderLineEdit.setGeometry(QRect(130, 100, 431, 41))
        font2 = QFont()
        font2.setPointSize(10)
        self.OutputFolderLineEdit.setFont(font2)
        self.ChooseOutputFolderButton = QPushButton(self.folderChooserGroupbox)
        self.ChooseOutputFolderButton.setObjectName(u"ChooseOutputFolderButton")
        self.ChooseOutputFolderButton.setGeometry(QRect(20, 100, 101, 41))
        self.ChooseOutputFolderButton.setFont(font2)
        self.ChooseOutputFolderButton.setFocusPolicy(Qt.WheelFocus)
        self.InputFolderLineEdit = QLineEdit(self.folderChooserGroupbox)
        self.InputFolderLineEdit.setObjectName(u"InputFolderLineEdit")
        self.InputFolderLineEdit.setEnabled(False)
        self.InputFolderLineEdit.setGeometry(QRect(130, 40, 431, 41))
        self.InputFolderLineEdit.setFont(font2)
        self.ChooseInputFolderButton = QPushButton(self.folderChooserGroupbox)
        self.ChooseInputFolderButton.setObjectName(u"ChooseInputFolderButton")
        self.ChooseInputFolderButton.setGeometry(QRect(20, 40, 101, 41))
        self.ChooseInputFolderButton.setFont(font2)
        self.ChooseInputFolderButton.setAutoDefault(False)
        self.ChooseInputFolderButton.setFlat(False)
        self.ExtraFileOptionsGroupbox = QGroupBox(self.centralwidget)
        self.ExtraFileOptionsGroupbox.setObjectName(u"ExtraFileOptionsGroupbox")
        self.ExtraFileOptionsGroupbox.setGeometry(QRect(390, 210, 261, 261))
        self.ExtraFileOptionsGroupbox.setFont(font1)
        self.CopyMetadataCheckbox = QCheckBox(self.ExtraFileOptionsGroupbox)
        self.CopyMetadataCheckbox.setObjectName(u"CopyMetadataCheckbox")
        self.CopyMetadataCheckbox.setGeometry(QRect(10, 100, 231, 51))
        self.CopyMetadataCheckbox.setChecked(True)
        self.IncludeNonAudioCheckbox = QCheckBox(self.ExtraFileOptionsGroupbox)
        self.IncludeNonAudioCheckbox.setObjectName(u"IncludeNonAudioCheckbox")
        self.IncludeNonAudioCheckbox.setGeometry(QRect(10, 30, 231, 61))
        self.IncludeNonAudioCheckbox.setChecked(True)
        self.AboutButton = QPushButton(self.centralwidget)
        self.AboutButton.setObjectName(u"AboutButton")
        self.AboutButton.setGeometry(QRect(380, 500, 231, 61))
        self.AboutButton.setFont(font)
        self.AboutButton.setFocusPolicy(Qt.WheelFocus)
        self.ConversionOptionsGroupBox = QGroupBox(self.centralwidget)
        self.ConversionOptionsGroupBox.setObjectName(u"ConversionOptionsGroupBox")
        self.ConversionOptionsGroupBox.setGeometry(QRect(20, 210, 351, 261))
        self.ConversionOptionsGroupBox.setFont(font1)
        self.InputFileFormatComboBox = QComboBox(self.ConversionOptionsGroupBox)
        self.InputFileFormatComboBox.setObjectName(u"InputFileFormatComboBox")
        self.InputFileFormatComboBox.setGeometry(QRect(20, 60, 311, 31))
        self.InputFileFormatLabel = QLabel(self.ConversionOptionsGroupBox)
        self.InputFileFormatLabel.setObjectName(u"InputFileFormatLabel")
        self.InputFileFormatLabel.setGeometry(QRect(20, 30, 121, 31))
        self.InputFileFormatLabel.setFont(font1)
        self.InputFileFormatLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.OutputFileFormatLabel = QLabel(self.ConversionOptionsGroupBox)
        self.OutputFileFormatLabel.setObjectName(u"OutputFileFormatLabel")
        self.OutputFileFormatLabel.setGeometry(QRect(20, 100, 121, 31))
        self.OutputFileFormatLabel.setFont(font1)
        self.OutputFileFormatLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.OutputFileFormatComboBox = QComboBox(self.ConversionOptionsGroupBox)
        self.OutputFileFormatComboBox.setObjectName(u"OutputFileFormatComboBox")
        self.OutputFileFormatComboBox.setGeometry(QRect(20, 130, 311, 31))
        self.OutputFileParametersLabel = QLabel(self.ConversionOptionsGroupBox)
        self.OutputFileParametersLabel.setObjectName(u"OutputFileParametersLabel")
        self.OutputFileParametersLabel.setGeometry(QRect(20, 170, 311, 31))
        self.OutputFileParametersLabel.setFont(font1)
        self.OutputFileParametersLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.OutputFileParametersComboBox = QComboBox(self.ConversionOptionsGroupBox)
        self.OutputFileParametersComboBox.setObjectName(u"OutputFileParametersComboBox")
        self.OutputFileParametersComboBox.setGeometry(QRect(20, 200, 311, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.folderChooserGroupbox.raise_()
        self.progressBar.raise_()
        self.StatusLabel.raise_()
        self.RunButton.raise_()
        self.ExtraFileOptionsGroupbox.raise_()
        self.AboutButton.raise_()
        self.ConversionOptionsGroupBox.raise_()

        self.retranslateUi(MainWindow)

        self.RunButton.setDefault(False)
        self.ChooseOutputFolderButton.setDefault(False)
        self.ChooseInputFolderButton.setDefault(False)
        self.AboutButton.setDefault(False)


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
        self.ExtraFileOptionsGroupbox.setTitle(QCoreApplication.translate("MainWindow", u"Additional File Options", None))
        self.CopyMetadataCheckbox.setText(QCoreApplication.translate("MainWindow", u"Attempt to copy file metadata\n"
"(e.g., tags) to transcoded files", None))
        self.IncludeNonAudioCheckbox.setText(QCoreApplication.translate("MainWindow", u"Copy non-audio files\n"
"(e.g., images, log files, etc.)\n"
"to output folder(s)", None))
        self.AboutButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.ConversionOptionsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Conversion Options", None))
        self.InputFileFormatLabel.setText(QCoreApplication.translate("MainWindow", u"Input Format", None))
        self.OutputFileFormatLabel.setText(QCoreApplication.translate("MainWindow", u"Output Format", None))
        self.OutputFileParametersLabel.setText(QCoreApplication.translate("MainWindow", u"Output Encoding Options", None))
    # retranslateUi

