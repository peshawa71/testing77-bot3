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
from moviepy.editor import *

# Load your video
clip = VideoFileClip("main_video.mp4")

# Cut the first 10 seconds
clip = clip.subclip(0, 10)

# Add text overlay
txt = TextClip("Edited with MoviePy", fontsize=40, color="white")
txt = txt.set_position(("center", "bottom")).set_duration(clip.duration)

# Combine video + text
final = CompositeVideoClip([clip, txt])

# Export the result
final.write_videofile("edited.mp4", codec="libx264", fps=24)


