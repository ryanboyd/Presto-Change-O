# ![Magic!](https://github.com/Red-Warlock/Presto-Change-O/blob/main/resources/images/magic-wand-64x64.png) Presto Change-O

## About
 Presto Change-O is a GUI program for batch converting audio files from one format to another. This software is primarily intended for people who do not have any programming experience, are not particularly savvy with computers, or just generally don't want to spend their time/energy learning about how to use transcoding tools. Made primarily in Python.

## Status
This program should always be thought of as a work in progress. If there are formats/settings that you would like to see added or changed, please contact the software author

## How to Use
The software itself is intended to be quite straight-forward and assumes that you have some audio files that you would like to convert from one format to another. As such, you need to tell the application at least 4 things:

1. The location of the files that you would like to transcode into another format
2. The location where you would like your converted files to be saved
3. The file format of the input files that you are transcoding
4. The format that you would like to transcode your files into

Depending on what type of file you would like to get as output, you may be asked to choose some basic parameters for the transcoding process. For example, if you are converting some FLAC files to MP3 files, you will be given a selection of transcoding options for the quality of the MP3 files (for example, Variable Bitrate versus Constant Bitrate). In most cases, the default selection provided by the software is likely ideal for most people.

Once you have set the appropriate options above, simply click the **Convert Files!** button and the software should handle the rest.

## Adding Additional Formats
If you would like to add new formats and have a decent grasp of how ffmpeg works, you can add new format files to the **audio_format_configs** application folder. The format of these files is fairly straight-forward and self-explanatory, and you should be able to simply copy an existing file and modify it to your liking. However, if there is a format that you would like to have added to Presto Change-O as a default pack-in, please just let me know.

## Troubleshooting
While the software runs, it saves an output log generated during the conversion process to a file named **log-conversions.txt**. If you are encountering problems (for example, files not converting correctly, or files not converting at all), this log should be the first place that you look. If you need to request help or post an issue, it will be helpful if you share your log file so that I can see what is going wrong.

## A Note about Lossy versus Lossless Formats

For the user who is *very* unfamiliar with audio file formats, it is important to understand the distinction between formats that are perfect, one-to-one copies of the source material (i.e., lossless, such as FLAC files) versus files that remove some of the original audio data to make the files smaller (i.e., lossy, such as MP3 files). A complete discussion on the technical aspects and implications of lossless vs. lossy file formats is beyond the scope of this README, however, it is important to note that it is generally poor form to convert from lossy formats to lossless formats. There are some exceptions to this (for example, if you are working with a program or hardware that *reqires* a WAV file specifically, you may need to convert your MP3 to a lossless WAV file. However, outside of these rare circumstances, it is advised that you only convert *to* lossless formats *from* other lossless formats.

For curious readers, a fairly gentle introduction to the topic can be found here:
https://www.headphonesty.com/2020/04/best-audio-file-formats-explained/

# Disclaimer

Use this software at your own risk. Ryan Boyd disclaims all warranties, expressed or implied, including, without limitation, the warranties of merchant ability and of fitness for any purpose. Neither Ryan Boyd nor anyone else who has been involved in the creation, production or delivery of this software assumes any liability for damages, direct or consequential, which may result from your use of the software.

# Acknowledgements
 - The actual brains that drive this application is [ffmpeg](https://ffmpeg.org/), a super powerful multimedia tool made by people far smarter than me. If this software is helpful and you would like to give back, please consider [donating to ffmpeg](https://ffmpeg.org/donations.html).
 - Red Warlock artwork courtesy of [Wikimedia Commons](https://en.wikipedia.org/wiki/File:Grand_Warlock_of_Wikipedia.png)
 - The UI of this application is driven by the [Qt framework](https://www.qt.io/).