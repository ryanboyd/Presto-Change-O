from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, Signal, Slot, SLOT, SIGNAL, QObject, QSize

from config import Config
from qt6_forms.main_window import Ui_MainWindow

from AudioConverter import AudioConverter
from show_messageboxes import *
from show_about import ShowAbout


class MainWindow(QMainWindow):

    inputFolder = 'C:/Users/ahitp/Downloads/Carpenter Brut'
    outputFolder = 'C:/Users/ahitp/Downloads/output'

    msgBox = MessageBoxShower(appId=Config.myappid)

    audioConverter = AudioConverter()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Connect the input and output folder buttons with functions used to call file browsers
        self.ui.ChooseInputFolderButton.clicked.connect(self.ChooseInputFolder)
        self.ui.ChooseOutputFolderButton.clicked.connect(self.ChooseOutputFolder)

        #connect the About button with the correct function
        self.ui.AboutButton.clicked.connect(ShowAbout)

        #connect the run button with the appropriate function
        self.ui.RunButton.clicked.connect(self.RunConversions)

        if self.inputFolder is not None and self.inputFolder != "":
            self.ui.InputFolderLineEdit.setText(self.inputFolder)
        if self.outputFolder is not None and self.outputFolder != "":
            self.ui.OutputFolderLineEdit.setText(self.outputFolder)


    @Slot()
    def ChooseInputFolder(self):

        folderChooser = QFileDialog()

        if self.inputFolder != None and self.inputFolder != "":
            folderChooser.setDirectory(self.inputFolder)

        self.inputFolder = folderChooser.getExistingDirectory(self, "Choose your input folder")
        self.ui.InputFolderLineEdit.setText(self.inputFolder)
        return

    @Slot()
    def ChooseOutputFolder(self):

        folderChooser = QFileDialog()

        if self.outputFolder != None and self.outputFolder != "":
            folderChooser.setDirectory(self.outputFolder)

        self.outputFolder = folderChooser.getExistingDirectory(self,"Choose your output folder")
        self.ui.OutputFolderLineEdit.setText(self.outputFolder)
        return


    @Slot()
    def RunConversions(self):

        if self.audioConverter.isRunning():
            self.audioConverter.awaitingTermination = True
            return

        if self.inputFolder == None or self.inputFolder == "":
            self.msgBox.ShowErrorMessageBox(error_msg="You must choose an input folder. Without an input folder"
                                                      " selected, I do not know where to look for the files that"
                                                      " you would like to convert.")
            return

        if self.outputFolder == None or self.outputFolder == "":
            self.msgBox.ShowErrorMessageBox(error_msg="You must choose an output folder. Without an output folder"
                                                      " selected, I do not know where to export your converted files.")
            return

        if Path(self.inputFolder) in Path(self.outputFolder).parents:
            self.msgBox.ShowErrorMessageBox(error_msg="Your output folder cannot be a subdirectory of your input"
                                                      " folder. This would create a problem where newly-created"
                                                      " output folders are also treated as additional input folders.")
            return

        if Path(self.inputFolder) == Path(self.outputFolder):
            self.msgBox.ShowErrorMessageBox(error_msg="Your output folder cannot be the sames as your input folder."
                                                      " Please choose (or create) a new folder for your converted"
                                                      " output files.")
            return


        self.ui.progressBar.setValue(0)
        self.ui.StatusLabel.setText("Running...")

        self.audioConverter.inputFolder = self.inputFolder
        self.audioConverter.outputFolder = self.outputFolder
        self.audioConverter.copyNonAudio = self.ui.IncludeNonAudioCheckbox.isChecked()
        self.audioConverter.copyMetaData = self.ui.CopyMetadataCheckbox.isChecked()

        #link up the emit with the progress bar
        QObject.connect(self.audioConverter, SIGNAL("progress(int)"), self.ui.progressBar,
                        SLOT("setValue(int)"), Qt.QueuedConnection)

        #link up the "update status bar" signal with the corresponding Slot
        self.audioConverter.signals.report_status.connect(self.StatusReport)

        #link up the ".finished" signal with the "FinishedConversions" function
        self.audioConverter.finished.connect(self.FinishedConversions)

        self.DisableControls()
        self.audioConverter.start()

        return


    @Slot()
    def StatusReport(self, statusText):
        self.ui.StatusLabel.setText(statusText)
        return


    @Slot()
    def FinishedConversions(self):

        self.ui.progressBar.setValue(100)
        self.ui.StatusLabel.setText("Finished!")

        self.msgBox.ShowInformationMessageBox(info_msg="The conversion process has completed.")

        self.ui.progressBar.setValue(0)
        self.ui.StatusLabel.setText("Waiting to process...")
        self.EnableControls()

        self.audioConverter = AudioConverter()

        return


    def EnableControls(self):
        self.ui.ChooseInputFolderButton.setEnabled(True)
        self.ui.ChooseOutputFolderButton.setEnabled(True)
        self.ui.IncludeNonAudioCheckbox.setEnabled(True)
        self.ui.RunButton.setText("Convert Files!")
        return

    def DisableControls(self):
        self.ui.ChooseInputFolderButton.setEnabled(False)
        self.ui.ChooseOutputFolderButton.setEnabled(False)
        self.ui.IncludeNonAudioCheckbox.setEnabled(False)
        self.ui.RunButton.setText("Cancel")
        return