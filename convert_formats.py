import os
from shutil import copyfile
from subprocess import Popen, PIPE, STARTUPINFO, STARTF_USESHOWWINDOW

from PySide6.QtCore import QThread, SIGNAL, Signal, QObject

#Because pydub relies on ffmpeg, we want to make sure that we have access to it before we import
#anything from the pydub package. Here, we check to see whether it's already in the PATH var and,
#if not, we go ahead and add it.
ffmpeg_bin_path = os.path.join(os.getcwd(), "external_apps/ffmpeg-5.0.1-essentials_build/bin/")

if ffmpeg_bin_path not in os.path.expandvars(os.getenv("PATH")).split(os.pathsep):
    print("Adding ffmpeg directory to PATH")
    os.environ["PATH"] += os.pathsep + ffmpeg_bin_path


class AudioConverter(QThread):
    __errorHappened = False

    inputFolder = None
    outputFolder = None
    copyNonAudio = False
    signals = None

    awaitingTermination = False

    startupinfo = STARTUPINFO()
    startupinfo.dwFlags |= STARTF_USESHOWWINDOW

    CREATE_NO_WINDOW = 0x08000000

    #we have to specify this signal in order to call it later
    update_status = Signal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.exiting = False
        self.signals = WorkerSignals()

    def run(self):
        self.FLAC_to_WAV()


    def FLAC_to_WAV(self):

        with open('log-conversions.txt', 'w', encoding='utf-8') as logfile_out:

            if not os.path.exists(self.outputFolder):
                os.mkdir(self.outputFolder)

            total_number_of_files = float(sum([len(files) for r, d, files in os.walk(self.inputFolder)]))
            files_processed_counter = 0

            for root, subdirs, files in os.walk(self.inputFolder):
                for single_file in files:

                    if self.awaitingTermination:
                        break

                    if single_file.lower().endswith('.flac'):

                        #print(f"Converting {single_file}...")
                        self.signals.report_status.emit(f"Converting {single_file}...")

                        outDir = root.replace(self.inputFolder, self.outputFolder)

                        if not os.path.exists(outDir):
                            os.mkdir(outDir)

                        fileIn = os.path.join(root, single_file)
                        fileOut = os.path.join(outDir, single_file.replace('.flac', '.wav'))

                        ffmpeg_cmd_to_execute = ["ffmpeg",
                                                 "-y",
                                                 "-i", fileIn,
                                                 "-map_metadata", "0",
                                                 "-id3v2_version", "3",
                                                 fileOut,
                                                 ]

                        #subprocess.call(ffmpeg_cmd_to_execute, creationflags=self.CREATE_NO_WINDOW)
                        p = Popen(ffmpeg_cmd_to_execute, stdin=PIPE, stdout=logfile_out, stderr=logfile_out,
                                  startupinfo=self.startupinfo,
                                  universal_newlines=True)
                        output, err = p.communicate()
                        rc = p.returncode


                    else:

                        if self.copyNonAudio:

                            #print(f"Copying {single_file}...")
                            self.signals.report_status.emit(f"Copying {single_file}...")

                            outDir = os.path.join(root.replace(self.inputFolder, self.outputFolder))
                            os.path.join(outDir, single_file)

                            if not os.path.exists(outDir):
                                os.mkdir(outDir)

                            copyfile(os.path.join(root, single_file), os.path.join(outDir, single_file))

                    files_processed_counter += 1

                    #report our conversion progress
                    if total_number_of_files != 0:

                        progressPct = int((files_processed_counter / total_number_of_files) * 100)

                        self.emit(SIGNAL("progress(int)"), progressPct)

                if self.awaitingTermination:
                    break

        self.awaitingTermination = False
        return


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.
    '''

    report_status = Signal(str)