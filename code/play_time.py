import json
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import math
from moviepy.editor import VideoFileClip
import os
import math

main_folder = '/media/ziwei/yuankai/RGB_video'
def size_all_counter(folder, video_files):
    total_size = 0
    for f in video_files:
        file_path = os.path.join(folder, f)
        total_size += os.path.getsize(file_path)
    return total_size

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def get_total_play_time(folder, video_files):
    total_play_time = 0.0
    for f in video_files:
        file_path = os.path.join(folder, f)
        clip = VideoFileClip(file_path)
        total_play_time += clip.duration
    return total_play_time

def convert_seconds_to_hms(seconds):
    # the 
    hours, remainder = divmod(seconds, 3600)
    # the minutes and seconds
    minutes, seconds = divmod(remainder, 60)
    return int(hours), int(minutes), seconds


# Rest of your code...
total_size = 0
total_play_time = 0.0  # in seconds
for folder in os.listdir(main_folder):
    folder_path = os.path.join(main_folder, folder)
    if os.path.isdir(folder_path):
        for folder2 in os.listdir(folder_path):
            folder_path2 = os.path.join(folder_path, folder2)
            if os.path.isdir(folder_path2):
                video_files = [f for f in os.listdir(folder_path2) if f.endswith('.mp4')]
                folder_size = size_all_counter(folder_path2, video_files)
                total_size += folder_size
                folder_play_time = get_total_play_time(folder_path2, video_files)
                total_play_time += folder_play_time
total_hours, total_minutes, total_seconds = convert_seconds_to_hms(total_play_time)
print(f"Total size: {convert_size(total_size)}")
print(f"Total play time: {total_hours} hours, {total_minutes} minutes, {total_seconds} seconds")