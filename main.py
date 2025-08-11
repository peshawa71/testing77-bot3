import subprocess

input_file = "input.mp4"
output_file = "main_video.mp4"

# Trim from 5 to 10 seconds without re-encoding (super fast)
cmd = [
    "ffmpeg",
    "-i", input_file,     # input file
    "-ss", "5",           # start time
    "-to", "10",          # end time
    "-c", "copy",         # copy streams (no re-encoding)
    output_file
]

subprocess.run(cmd, check=True)
print("Video edited and saved as", output_file)
