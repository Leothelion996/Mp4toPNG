import os
import subprocess
import re
from pathlib import Path


# *** Change Variable FFMPEG_PATH if your FFmeg is not in the default location. ***
FFMPEG_PATH = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"


def set_input_dir(directory):
    global INPUT_DIR
    INPUT_DIR = directory

def set_output_dir(directory):
    global OUTPUT_DIR
    OUTPUT_DIR = directory

def set_resolution(width, height):
    global RESIZE_FILTER
    RESIZE_FILTER = f"scale={width}:{height}"

def set_frame_rate(frame_rate):
    global FRAME_RATE
    FRAME_RATE = frame_rate

# extract frames from the input directory
def extract_frames():
    SCRIPT_DIR = str(Path(__file__).resolve().parent)
    INVALID_CHARS = re.escape(''.join([chr(i) for i in range(32)] + [':', '*', '?', '"', '<', '>', '|']))
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    video_files = [file for file in os.listdir(INPUT_DIR) if file.endswith(".mp4")]
    
    for video_file in video_files:
        input_path = os.path.join(INPUT_DIR, video_file)
        clean_name = re.sub(f'[{INVALID_CHARS}]', '', os.path.splitext(video_file)[0])
        output_folder = os.path.join(OUTPUT_DIR, clean_name)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        output_path = os.path.join(output_folder, "image%d.png")
        subprocess.run([FFMPEG_PATH, "-i", input_path, "-r", str(FRAME_RATE), "-vf", RESIZE_FILTER, output_path])

    print("Done!")


# Function to get values from UI and call extract_frames()
def start_conversion(app):
    set_input_dir(app.input_path.get())
    set_output_dir(app.output_path.get())
    resolution = app.resolution_var.get().split(":")
    set_resolution(resolution[0], resolution[1])
    set_frame_rate(app.framerate_var.get())
    extract_frames()
