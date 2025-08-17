# import subprocess
# print("may its working")

# input_file = "main_video.mp4"
# output_file = "hhhhh.mp4"

# # Trim from 5 to 10 seconds without re-encoding (super fast)
# cmd = [
#     "ffmpeg",
#     "-i", input_file,     # input file
#     "-ss", "5",           # start time
#     "-to", "10",          # end time
#     "-c", "copy",         # copy streams (no re-encoding)
#     output_file
# ]

# subprocess.run(cmd, check=True)
# print("Video edited and saved as", output_file)

# main.py
import os
from moviepy.editor import VideoFileClip

video_path = "main_video.mp4"

# Check if file exists
if not os.path.exists(video_path):
    raise FileNotFoundError(f"The file '{video_path}' does not exist!")

# If it exists, proceed
clip = VideoFileClip(video_path)

# Cut 5s → 15s
cut = clip.subclip(5, 15)

# Export
cut.write_videofile("cut.mp4", codec="libx264", audio_codec="aac", fps=24)
