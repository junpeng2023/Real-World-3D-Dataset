import cv2

video = cv2.VideoCapture('/media/ziwei/yuankai/RGB_video_120/col/col_coffee/coffee_two11_2022-10-17-18-29-32_camera_color_image_raw_compressed.mp4')

# Get video FPS
fps = video.get(cv2.CAP_PROP_FPS)

print(f'Video FPS: {fps}')

video.release()