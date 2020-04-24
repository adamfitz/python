"""
Script recursively search video files and based on filename extension attempt
to re encode the audio to mp3 using ffmpeg command:

ffmpeg -i "source_filename" -acodec mp3 -vcodec copy "target_filename"

"""

import subprocess
import os
import logging
from pathlib import Path


logging.basicConfig(level=logging.ERROR)

# set current directory
directory = os.getcwd()

# files in working dir and sub dirs
pathlist = Path(directory).glob('**/*')

file_ext = (".mkv", ".mp4", ".avi", ".webm")

try:
    for all_files in pathlist:
        # all_files is an object not a string
        file_and_path = (str(all_files))
        # original filename and path = file_and_path
        # determine if video file based on file extension
        if file_and_path.endswith(file_ext) and "re-encode" not in file_and_path:

            # original filename only = filename
            filename = str((file_and_path.split("/"))[-1])

            # full target dir
            target_dir = f"{directory}/{str((file_and_path.split('/'))[-2])}"

            # split name at the period
            target_list = filename.rsplit(".", 1)

            # target filename = build string with _re-encode_ in the name
            target_filename = f"{target_list[0]}_re-encode_.{target_list[1]}"
            try:
                logging.info(f"Converting audio to mp3:\n"
                             f"Input File:\t{file_and_path}\n"
                             f"Output File:\t{target_dir}/{target_filename}\n")
                # attempt re-encode audio to mp3 keeping video intact
                subprocess.run(
                    ["ffmpeg", "-i", f"{file_and_path}", "-acodec", "mp3",
                     "-vcodec", "copy", f"{target_dir}/{target_filename}", "-y"])
                print(f"")
            except Exception as broken:
                logging.error("something broke attempting to re encode audio")
except KeyboardInterrupt as user_interrupt:
    logging.error("\nUser interrupt actions not completed for the "
                  "following file:\n"
                  f"Input File:\t{file_and_path}\n"
                  f"Output File:\t{target_dir}/{target_filename}\n")
