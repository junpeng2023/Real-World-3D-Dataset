# import cv2
# import numpy
# size=(1280,720)

# videowrite = cv2.VideoWriter('./reading_mp4_demo/test.mp4',-1,30,size)
# img_array=[]

# for i in range(568):#这个循环是为了读取所有要用的图片文件
#     for filename in [r'./mp4_demo_images/'+str(i).zfill(4)+'.PNG' for i in range(568)]:#这个循环是为了读取所有要用的图片文件

#      img = cv2.imread(filename)
#      img_array.append(img)
    
# for i in range(568):#把读取的图片文件写进去
#     videowrite.write(img_array[i])
# videowrite.release()
# print('end!')
import cv2
import os

from PIL import Image


# image_folder='/home/adrian0909/FP/Procedure/ziwei_demo/mp4_col_demo'

image_folder= '/home/ziwei/FP_plus/pictures/col'

# if os.path.exists(image_folder):
try:
    print('image folder exist')
    image_list=os.listdir(image_folder)
    print(image_list)
    image_num=len(image_list) 
    img = cv2.imread(os.path.join(image_folder,image_list[0]))
    imginfo = img.shape
    size = (imginfo[1], imginfo[0])  # 与默认不同，opencv使用 height在前，width在后，所有需要自己重新排序
    print(size)

    # 创建写入对象，包括 新建视频名称，每秒钟多少帧图片(10张) ,size大小
    # 一般人眼最低分辨率为19帧/秒
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G') #opencv3.0
    # videoWrite = cv2.VideoWriter( '/home/ziwei/FP_plus/example_col_coffee.mp4', fourcc, 30, size )
    
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    videoWrite = cv2.VideoWriter('/home/ziwei/FP_plus/example_col_coffee.mp4', fourcc, 30, size)

    for i in range(image_num):
        filename = '/home/ziwei/FP_plus/pictures/col' + str(i).zfill(4) + '.PNG'
        img = cv2.imread(filename) #ää # 1 表示彩图，0表示灰度图

        # 直接写入图片对应的数据
        videoWrite.write(img)

    videoWrite.release()  # 关闭写入对象
    print('end')
except IOError:
    print('The image file can not be opened')
        




