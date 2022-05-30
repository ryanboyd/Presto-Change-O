import config

class AudioFormat():

    format_name: str
    file_extension: str
    is_input_type: bool
    is_output_type: bool
    ffmpeg_commands: dict
    encoding_options: list
    default_setting: str
    required_output_params: list
    required_input_params: list


    def __init__(self, format_name: str, file_extension: str,
                 ffmpeg_commands: list, encoding_options: list,
                 is_input_type: bool, is_output_type: bool,
                 default_setting: str, required_output_params: list,
                 required_input_params: list):

        self.format_name = format_name
        self.file_extension = file_extension
        self.ffmpeg_commands = ffmpeg_commands
        self.encoding_options = encoding_options
        self.is_input_type = is_input_type
        self.is_output_type = is_output_type
        self.default_setting = default_setting
        self.required_output_params = required_output_params
        self.required_input_params = required_input_params

def get_audio_format(audio_format: str) -> AudioFormat:
    return config.file_formats[audio_format]


