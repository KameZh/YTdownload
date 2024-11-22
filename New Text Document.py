import os
import subprocess

ffmpeg_path = "C:\\ffmpeg\\bin"  # Replace this with the path to your FFmpeg 'bin' folder.

# Add FFmpeg to the PATH permanently
subprocess.run(f'setx PATH "%PATH%;{ffmpeg_path}"', shell=True)

# Verify FFmpeg installation
print("FFmpeg has been added to your PATH. Verifying installation...")
subprocess.run("ffmpeg -version", shell=True)
