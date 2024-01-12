import cv2
import os

video_folder = '/media/ziwei/yuankai/RGB_video'
max_frames = 0
max_frames_video = ''

for folder_name_1 in os.listdir(video_folder):
    folder_path_1 = os.path.join(video_folder, folder_name_1)
    for folder_name_2 in os.listdir(folder_path_1):
        folder_path_2 = os.path.join(folder_path_1, folder_name_2)
        for video_file in os.listdir(folder_path_2):
            video_path = os.path.join(folder_path_2, video_file)
            video = cv2.VideoCapture(video_path)
            frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

            if frames > max_frames:
                max_frames = frames
                max_frames_video = video_path

            video.release()

print(f'The video with the maximum frames is {max_frames_video} with {max_frames} frames.')