import os

# Directory containing the frames
frame_directory = '/media/ziwei/PortableSSD/depth_data/depth_frames/single/single_working/single_working_5'

# Get all the .png files in the directory
all_files = [f for f in os.listdir(frame_directory) if f.endswith('.png')]

# Sort the files based on the timestamp in the filename
sorted_files = sorted(all_files, key=lambda x: int(x.split('_')[1]))

# Rename each file
for idx, filename in enumerate(sorted_files, 1):
    old_path = os.path.join(frame_directory, filename)
    new_name = f"depth_frame_{idx}.png"
    new_path = os.path.join(frame_directory, new_name)
    os.rename(old_path, new_path)

print("Renaming completed!")