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
from moviepy.editor import VideoFileClip

clip = VideoFileClip("main_video.mp4")
cut = clip.subclip(5, 15)   # cut from 5s to 15s
cut.write_videofile("cut.mp4", codec="libx264", fps=24)


