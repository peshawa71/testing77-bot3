import subprocess
print("may its working")

input_file = "https://github.com/peshawa71/testing77-bot3/blob/main/main_video.mp4"
output_file = "hhhhh.mp4"

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

