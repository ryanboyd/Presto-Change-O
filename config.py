import ctypes
import os
import json
import pathlib
import audio_formats

#name of our application
myappid = "Presto Change-O"

#important paths that we're going to work with
ffmpeg_bin_path = os.path.join(os.getcwd(), "external_apps/ffmpeg-5.0.1-essentials_build/bin/")
audio_format_configs_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "audio_format_configs")

#dictionary that holds all of our file conversion data for ffmpeg, etc.
file_formats = {}


def init():
    # Tell Windows that this is its own application and not just pythonw.exe
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    #load in all of the configs for each audio format
    for filename in os.listdir(audio_format_configs_dir):

        filename_extension = pathlib.Path(filename.lower()).suffix

        if filename_extension  == ".json":

            with open(os.path.join(audio_format_configs_dir, filename), 'r', encoding='utf-8') as file_in:
                config_data = json.load(file_in)


                newAudioFormat = audio_formats.AudioFormat(format_name=config_data["format_name"],
                                                           file_extension=config_data["file_extension"],
                                                           ffmpeg_commands=config_data["ffmpeg_commands"],
                                                           encoding_options=list(config_data["ffmpeg_commands"].keys()),
                                                           is_input_type=config_data["is_input_type"],
                                                           is_output_type=config_data["is_output_type"])

                file_formats[newAudioFormat.format_name] = newAudioFormat


    #make sure that ffmpeg is in our path
    if ffmpeg_bin_path not in os.path.expandvars(os.getenv("PATH")).split(os.pathsep):
        print("Adding ffmpeg directory to PATH")
        os.environ["PATH"] += os.pathsep + ffmpeg_bin_path




