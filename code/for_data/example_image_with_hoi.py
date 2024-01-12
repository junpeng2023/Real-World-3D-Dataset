import cv2
import numpy as np
import os
import numpy as np
import json

action_label=["idle","approach","leave","move","take","place","pour","cut","stir","wipe","drink","eat","wear","open","read","write","squeeze","smell","close","spray","prune","play","talk","peel","comb","brush","shave"]
object_label_global=["human1","human2","cup","milk","coffee","scoop","sugar","kettle","honey","bowl","tee bag","cereal","rag","glasses","pencil","notebook","newspaper","phone","flower","plants","container","shears","computer","ipad","place mat","bread","plate","knife","chopping block","apple","banana","peeler","mirror","comb","toothbrush","toothpaste","shaver"]


#bounding box yolo format to voc format
def yolo2voc(bboxes, image_height, image_width):
    """
    yolo => [xmid, ymid, w, h] (normalized)
    voc  => [x1, y1, x2, y2]
    """
    bboxes = bboxes.copy().astype(float)  # otherwise all value will be 0 as voc_pascal dtype is np.int

    w = bboxes[2] * image_width
    h = bboxes[3] * image_height

    x_min=bboxes[0]*image_width-w/2
    y_min=bboxes[1]*image_height-h/2

    bboxes=[x_min,y_min,x_min+w,y_min+h]

    return bboxes


def showGT(file):
    #first divide png and txt to different list
    png=[]
    txt=[]
    for f in os.listdir(file):
        if f.endswith('.PNG'):
            png.append(f)
        elif f.endswith('.txt'):
            txt.append(f)

    GTlist=txt
    GTlist.sort(key=lambda x:int(x[6:-4]))
    imglist = png
    imglist.sort(key=lambda x:int(x[6:-4]))
    # print(GTlist)
    img_num=len(imglist)
    GT_num=len(GTlist)
    # get the height and width of image
    imgpath=os.path.join(file,imglist[0])
    img=cv2.imread(imgpath)
    height=img.shape[0]
    width=img.shape[1]
    font=cv2.FONT_HERSHEY_SIMPLEX

    for j in range(img_num):
        # deal with mannual annotation of yolo format
        GT_path=os.path.join(file,GTlist[j])
        with open(GT_path,'r') as f:
            data=f.read()
            data=data.split()
            data=list(map(float,data))
        object_num=int(len(data)/5)
        bbox_list=[]
        for i in range(object_num):
            bbox_list.append([data[1+i*5],data[2+i*5],data[3+i*5],data[4+i*5]])

        bbox_list=np.array(bbox_list)
        #load frame
        img_path=os.path.join(file,imglist[j])
        image=cv2.imread(img_path)
        # create a list: for different class give different colors
        colors=[[255,255,255],[0,255,0],[255,0,0],[0,0,255],[255,255,0],[0,255,255],[255,0,255],[0,0,0],[100,40,50]]
        #draw bounding box in each frame
        for i in range(object_num):
            # colors=[i*20,i*30,i*5]
            a=bbox_list[i]
            bbox=yolo2voc(a,image_height=height,image_width=width)
            x1=int(bbox[0])
            y1=int(bbox[1])
            x2=int(bbox[2])
            y2=int(bbox[3])
            cv2.rectangle(image, (x1,y1),(x2,y2), colors[i],2)
            # cv2.putText(image,"current action:",(0,60), font,3, (0,255,0),2)

            # cv2.putText(image,"next action:",(0,120), font, 3, (0,0,255),2)
            # cv2.putText(image,"next action:",org
            #(0,60) 3, (0,255,0),15)
             
        cv2.imwrite('pictures_single_to_show/example'+'/'+str(j).zfill(4)+'.PNG', image)
        cv2.imshow('Ground Truth', image)
        cv2.waitKey(10) & 0xFF
    cv2.destroyAllWindows()

File="/media/ziwei/yuankai/yolo_output/task_9_pick_up/mp/mp_pick_up_2/obj_train_data"
showGT(File)