import json
import re

input_file = "mp3.json"

with open(input_file, 'r', encoding='utf-8') as fin:
    config_data = json.loads(fin.read())


if input_file == "mp3.json":
    config_data["ffmpeg_commands"] = {}

    for option in config_data['encoding_options']:
        if "Variable" in option:
            config_data["ffmpeg_commands"][option] = ["-q", re.findall(r'\d', option)[0]]
        else:
            config_data["ffmpeg_commands"][option] = ["-b", re.findall(r'\d+', option)[0] + 'k']

    with open("mp3-fix.json", 'w', encoding='utf-8') as fout:
        json.dump(config_data, fout, ensure_ascii=False, indent=4)