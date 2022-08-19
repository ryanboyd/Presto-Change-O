import os
import pathlib

from AudioFormatClass import *
from shutil import copyfile
from subprocess import Popen, PIPE

#this only is relevant if we're on a Windows computer. Otherwise,
#it will simply throw an exception as these are not subprocess members on other platforms.
if os.name == "nt":
    from subprocess import STARTUPINFO, STARTF_USESHOWWINDOW

from PySide6.QtCore import QThread, SIGNAL, Signal, QObject

import AudioFormatClass


class AudioConverter(QThread):
    __errorHappened = False

    #parameters used to run the conversion
    inputFolder: str
    outputFolder: str
    copyNonAudio: bool
    copyMetaData: bool
    input_audio_format: AudioFormat
    output_audio_format: AudioFormat
    encoding_settings: str

    if os.name=="nt":
        #These are all generally used to suppress terminal windows when calling ffmpeg
        startupinfo = STARTUPINFO()
        startupinfo.dwFlags |= STARTF_USESHOWWINDOW
        CREATE_NO_WINDOW = 0x08000000


    #specify a variable to hold all of the signals used in WorkerSignals()
    signals = None

    #used to terminate the thread when user hits cancel button
    userCancelled = False



    #we have to specify this signal in order to call it later
    update_status = Signal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.exiting = False
        self.signals = WorkerSignals()

    def run(self):
        self.userCancelled = False
        self.Perform_Conversions()
        return


    def Perform_Conversions(self):

        with open('log-conversions.txt', 'w', encoding='utf-8') as logfile_out:

            if not os.path.exists(self.outputFolder):
                os.makedirs(self.outputFolder)

            total_number_of_files = float(sum([len(files) for r, d, files in os.walk(self.inputFolder)]))
            files_processed_counter = 0

            for root, subdirs, files in os.walk(self.inputFolder):
                for single_file in files:

                    if self.userCancelled:
                        break

                    if pathlib.Path(single_file.lower()).suffix == self.input_audio_format.file_extension:

                        #print(f"Converting {single_file}...")
                        self.signals.report_status.emit(f"Converting {single_file}...")

                        outDir = root.replace(self.inputFolder, self.outputFolder)

                        if not os.path.exists(outDir):
                            os.makedirs(outDir)

                        #get the full path of the input file
                        fileIn = os.path.join(root, single_file)

                        #get the output file name
                        fileOut = os.path.join(outDir, single_file)
                        #...then change the extension to the new one
                        fileOut = os.path.splitext(fileOut)[0] + self.output_audio_format.file_extension

                        ffmpeg_cmd_to_execute = ["ffmpeg", "-y"]

                        #If there are required input parameters for this format (which is fairly rare),
                        #then we append them here
                        if self.input_audio_format.required_input_params is not None:
                            ffmpeg_cmd_to_execute.extend(self.input_audio_format.required_output_params)

                        #Now we add the input filename
                        ffmpeg_cmd_to_execute.extend(["-i", fileIn])

                        if self.copyMetaData:
                            ffmpeg_cmd_to_execute.extend(["-map_metadata", "0",
                                                          "-id3v2_version", "3"])

                        #if there are encoding settings that have been selected, then we add those to the
                        #command line call that we're going to make
                        if self.encoding_settings is not None:
                            ffmpeg_cmd_to_execute.extend(
                                self.output_audio_format.ffmpeg_commands[self.encoding_settings])

                        #If there are any required parameters, then we add those on as well
                        if self.output_audio_format.required_output_params is not None:
                            ffmpeg_cmd_to_execute.extend(
                                self.output_audio_format.required_output_params)


                        ffmpeg_cmd_to_execute.append(fileOut)

                        #subprocess.call(ffmpeg_cmd_to_execute, creationflags=self.CREATE_NO_WINDOW)
                        if os.name=="nt":
                            p = Popen(ffmpeg_cmd_to_execute, stdin=logfile_out, stdout=logfile_out, stderr=logfile_out,
                                  startupinfo=self.startupinfo,
                                  universal_newlines=True)
                        else:
                            p = Popen(ffmpeg_cmd_to_execute, stdin=logfile_out, stdout=logfile_out, stderr=logfile_out,
                                      shell=False, universal_newlines=True)
                        output, err = p.communicate()
                        rc = p.returncode


                    else:

                        if self.copyNonAudio:

                            #print(f"Copying {single_file}...")
                            self.signals.report_status.emit(f"Copying {single_file}...")

                            outDir = os.path.join(root.replace(self.inputFolder, self.outputFolder))
                            os.path.join(outDir, single_file)

                            if not os.path.exists(outDir):
                                os.makedirs(outDir)

                            copyfile(os.path.join(root, single_file), os.path.join(outDir, single_file))

                    files_processed_counter += 1

                    #report our conversion progress
                    if total_number_of_files != 0:

                        progressPct = int((files_processed_counter / total_number_of_files) * 100)

                        self.emit(SIGNAL("progress(int)"), progressPct)

                if self.userCancelled:
                    break

        return


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.
    '''

    report_status = Signal(str)