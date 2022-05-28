from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, Signal, Slot, SLOT, SIGNAL, QObject, QSize

import config
from audio_formats import get_audio_format
from qt6_forms.main_window import Ui_MainWindow

from AudioConverter import AudioConverter
from show_messageboxes import *
from show_about import ShowAbout


class MainWindow(QMainWindow):

    inputFolder = 'C:/Users/ahitp/Downloads/Carpenter Brut'
    outputFolder = 'C:/Users/ahitp/Downloads/output'

    msgBox = MessageBoxShower(appId=config.myappid)

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

        #connect the updating of the output filetype combobox with a function that updates
        #the encoding options combobox
        self.ui.OutputFileFormatComboBox.currentIndexChanged.connect(self.UpdateEncodingOptions)

        #if we're starting with pre-selected input/output directories, we just go ahead
        #and load those up/display them in the LineEdit boxes from the get-go
        if self.inputFolder is not None and self.inputFolder != "":
            self.ui.InputFolderLineEdit.setText(self.inputFolder)
        if self.outputFolder is not None and self.outputFolder != "":
            self.ui.OutputFolderLineEdit.setText(self.outputFolder)

        #add the formats to the appropriate comboboxes

        input_formats = []
        output_formats = []

        for audio_format in config.file_formats.keys():
            if get_audio_format(audio_format).is_input_type:
                input_formats.append(audio_format)
            if get_audio_format(audio_format).is_output_type:
                output_formats.append(audio_format)

        self.ui.InputFileFormatComboBox.addItems(input_formats)
        index = self.ui.InputFileFormatComboBox.findText("FLAC", Qt.MatchFixedString)
        if index >= 0:
            self.ui.InputFileFormatComboBox.setCurrentIndex(index)

        self.ui.OutputFileFormatComboBox.addItems(output_formats)
        index = self.ui.OutputFileFormatComboBox.findText("WAV", Qt.MatchFixedString)
        if index >= 0:
            self.ui.OutputFileFormatComboBox.setCurrentIndex(index)

        self.UpdateEncodingOptions()



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

        #prep the progress bar
        self.ui.progressBar.setValue(0)
        self.ui.StatusLabel.setText("Running...")

        #set up all of the parameters used during conversion
        self.audioConverter.inputFolder = self.inputFolder
        self.audioConverter.outputFolder = self.outputFolder
        self.audioConverter.copyNonAudio = self.ui.IncludeNonAudioCheckbox.isChecked()
        self.audioConverter.copyMetaData = self.ui.CopyMetadataCheckbox.isChecked()
        self.audioConverter.input_audio_format = get_audio_format(self.ui.InputFileFormatComboBox.currentText())
        self.audioConverter.output_audio_format = get_audio_format(self.ui.OutputFileFormatComboBox.currentText())
        if self.GetNumberOfEncodingOptions(self.ui.OutputFileFormatComboBox.currentText()) > 0:
            self.audioConverter.encoding_settings = self.ui.OutputFileParametersComboBox.currentText()
        else:
            self.audioConverter.encoding_settings = None

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
    def UpdateEncodingOptions(self):

        selectedFiletype = self.ui.OutputFileFormatComboBox.currentText()

        self.ui.OutputFileParametersComboBox.clear()
        self.ui.OutputFileParametersComboBox.addItems(get_audio_format(selectedFiletype).encoding_options)
        self.SetParameterComboBoxEnabledStatus()

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
        self.ui.CopyMetadataCheckbox.setEnabled(True)
        self.ui.InputFileFormatComboBox.setEnabled(True)
        self.ui.OutputFileFormatComboBox.setEnabled(True)
        self.SetParameterComboBoxEnabledStatus()
        self.ui.RunButton.setText("Convert Files!")
        return

    def DisableControls(self):
        self.ui.ChooseInputFolderButton.setEnabled(False)
        self.ui.ChooseOutputFolderButton.setEnabled(False)
        self.ui.IncludeNonAudioCheckbox.setEnabled(False)
        self.ui.CopyMetadataCheckbox.setEnabled(False)
        self.ui.InputFileFormatComboBox.setEnabled(False)
        self.ui.OutputFileFormatComboBox.setEnabled(False)
        self.ui.OutputFileParametersComboBox.setEnabled(False)
        self.ui.RunButton.setText("Cancel")
        return

    def GetNumberOfEncodingOptions(self, selectedFiletype: str) -> int:
        return len(get_audio_format(selectedFiletype).encoding_options)

    def SetParameterComboBoxEnabledStatus(self):
        '''
        This function checks to see if the output file format type has any associated options. If not, then the control
        is disabled. If so, then it is enabled.
        :return:
        '''
        selectedFiletype = self.ui.OutputFileFormatComboBox.currentText()
        if self.GetNumberOfEncodingOptions(selectedFiletype) > 0:
            self.ui.OutputFileParametersComboBox.setEnabled(True)
        else:
            self.ui.OutputFileParametersComboBox.setEnabled(False)
            self.ui.OutputFileParametersComboBox.addItems(["None Available"])