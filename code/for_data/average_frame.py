import cv2
import os

# Path to the directory containing the video files
directory = "/media/ziwei/yuankai/RGB_video"

# Initialize total frames count
total_frames = 0
video_count = 0  # Initialize the video count

# Loop over all video files in the directory

for folder_name_1 in os.listdir(directory):
    folder_path_1 = os.path.join(directory, folder_name_1)
    for folder_name_2 in os.listdir(folder_path_1):
        folder_path_2= os.path.join(folder_path_1, folder_name_2)
        for filename in os.listdir(folder_path_2):
            
            if filename.endswith(".mp4"):  # replace with your video file extension if not .mp4
                video = cv2.VideoCapture(os.path.join(folder_path_2, filename))

                # Get the total number of frames in the current video
                frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

                # Update the total frames count
                total_frames += frames

                # Update the total video count
                video_count += 1

                # Release the video file
                video.release()

# Calculate average frames per video
average_frames = total_frames / video_count if video_count > 0 else 0

print(f"Average frames per video: {average_frames}")