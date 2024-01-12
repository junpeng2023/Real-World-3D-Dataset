
from importlib.resources import path
from tkinter import Image
import cv2
import numpy as np
import os
import numpy as np
import json



from pandas.core.frame import DataFrame
with open('/home/adrian0909/FP/Procedure/engine/coffee_mp_2.json', 'r') as fcc_file:
     fcc_data = json.load(fcc_file)

print()    


action_label=["idle","approach","leave","move","take","place","pour","cut","stir","wipe","drink","eat","wear","open","read","write"]
object_label=["human","plate","bread","glasses","pencil","notebook","newspaper","cup"]
grund_truth=[0,[1,4],15,[4,3],40,[12,3],97,[1,6],107,[4,6],127,[14,6],300,[5,6],332,[1,7],349,[4,7],378,[10,7],425,[5,7],515,[2,7],531,[0,0],567]

# slice_num is the number of action slices.
slice_num=int(len(grund_truth)/2)
print(slice_num)
# To_print has the content of each action slices 
To_print=grund_truth[1::2]
print(To_print)

# add two elements to solve the prediction problem at the end stage.
To_print.append([0,0])
To_print.append([0,0])
# key frames used to distinguish the action slices
key_frames=grund_truth[::2]
print(key_frames)


# store length of each slices in slices_length
slices_length=[]
for n in range(1, len(key_frames)):
   slices_length.append(key_frames[n] - key_frames[n-1])

slices_length[0]+=1
print(slices_length)
slices_time=[x/30 for x in slices_length]
slices_time.append(0)
slices_time.append(0)
print(slices_time)

current_actuation_time=[]
next_actuation_time=[]
third_actuation_time=[]

frame_action_now=[]
frame_object_now=[]

frame_action_next=[]
frame_object_next=[]

frame_action_third=[]
frame_object_third=[]

total_length=grund_truth[-1]
key_number=0

key_frames=key_frames[1::]


# calculated the exation times 
for frame_change in key_frames : 
    slice_phase=slices_length[key_number]
    key_number+=1
   
    for i in range(slice_phase):
        

        current_actuation_time.append(((slice_phase-i)/slice_phase)*slices_time[key_number-1])
        next_actuation_time.append(slices_time[key_number])
        third_actuation_time.append(slices_time[key_number+1])
        frame_action_now.append(To_print[key_number-1][0])
        frame_object_now.append(To_print[key_number-1][1])
        frame_action_next.append(To_print[key_number][0])
        frame_object_next.append(To_print[key_number][1])
        frame_action_third.append(To_print[key_number+1][0])
        frame_object_third.append(To_print[key_number+1][1])



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




# give path of cvat result,contain png and txt files
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

        
        cv2.putText(image,"current action segment: "+"<" +"Human, " + action_label[frame_action_now[j]]+" ,"+object_label[frame_object_now[j]]+" ,"+str(format(current_actuation_time[j],'.3f'))+" >",(0,60), font,1, (0,255,0),2)
        cv2.putText(image,"next action segment: "+"<" +"Human, "+action_label[frame_action_next[j]]+" ,"+object_label[frame_object_next[j]]+" ,"+str(next_actuation_time[j])+" >",(0,120), font,1, (255,0,0) ,2)
        cv2.putText(image,"third action segment: "+"<" +"Human, "+action_label[frame_action_third[j]]+" ,"+object_label[frame_object_third[j]]+" ,"+str(third_actuation_time[j])+" >",(0,180), font,1, (0,128,255),2)
        #save the processesed images

        Image_name='/home/adrian0909/FP/Video_Production/kaige'+str(i).zfill(4)+'.PNG'

        
        
        cv2.imwrite('./mp4_demo_images'+'/'+str(j).zfill(4)+'.PNG', image)
        cv2.imshow('Ground Truth', image)
        cv2.waitKey(10) & 0xFF

   

    

    cv2.destroyAllWindows()


file='/home/adrian0909/FP/record/reading_with_person/obj_train_data'
showGT(file)


