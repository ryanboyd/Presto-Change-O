import ctypes
import os
import json
import pathlib
from AudioFormatClass import *

#name of our application
myappid = "Presto Change-O"

current_version = "1.00"

#important paths that we're going to work with
if os.name == "nt":
    ffmpeg_bin_path = os.path.join(os.getcwd(), "external_apps/ffmpeg-5.0.1-essentials_build-win/")
elif os.name == "posix":
    ffmpeg_bin_path = os.path.join(os.getcwd(), "external_apps/ffmpeg-5.0.1-mac/")

audio_format_configs_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "audio_format_configs")

#dictionary that holds all of our file conversion data for ffmpeg, etc.
file_formats = {}


def init():
    # Tell Windows that this is its own application and not just pythonw.exe
    if os.name=="nt":
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    #load in all of the configs for each audio format
    for filename in os.listdir(audio_format_configs_dir):

        filename_extension = pathlib.Path(filename.lower()).suffix

        if filename_extension == ".json":

            with open(os.path.join(audio_format_configs_dir, filename), 'r', encoding='utf-8') as file_in:

                try:
                    config_data = json.load(file_in)

                    newAudioFormat = AudioFormat(format_name=config_data["format_name"],
                                                               file_extension=config_data["file_extension"],
                                                               ffmpeg_commands=config_data["ffmpeg_commands"],
                                                               encoding_options=list(config_data["ffmpeg_commands"].keys()),
                                                               is_input_type=config_data["is_input_type"],
                                                               is_output_type=config_data["is_output_type"],
                                                               default_setting=config_data["default_setting"],
                                                               required_output_params=config_data["required_output_params"],
                                                               required_input_params=config_data["required_input_params"])

                    file_formats[newAudioFormat.format_name] = newAudioFormat

                except Exception as ex:
                    print(f"There was an error loading {filename}")
                    print(str(ex))


    #make sure that ffmpeg is in our path
    if ffmpeg_bin_path not in os.path.expandvars(os.getenv("PATH")).split(os.pathsep):
        print("Adding ffmpeg directory to PATH")
        os.environ["PATH"] += os.pathsep + ffmpeg_bin_path




