import cv2

video = cv2.VideoCapture('/media/ziwei/yuankai/RGB_video_120/col/col_coffee/coffee_two11_2022-10-17-18-29-32_camera_color_image_raw_compressed.mp4')

# Get video resolution (width and height)
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f'Video resolution: {frame_width} x {frame_height}')

video.release()
