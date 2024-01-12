import json
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
action_count_list = [0] * 27
print(action_count_list)





def action_all_counter(folder):
   json_files=[]
   for folder_name in os.listdir(folder):
      # folder_2=os.path.join(folder,folder_name)
      # if os.path.isdir(folder_2):
      #    for f in os.listdir(folder_2):
      if folder_name.endswith('.json'):
         json_files.append(folder_name)
   json_files.sort(key=lambda x:int(x[0:3]))
   file_number=len(json_files)
   #### changed
   print("The file numbers are:")
   print(file_number)
   ####
   # for folder_name in os.listdir(folder):
   #    folder_2=os.path.join(folder,folder_name)
   #    print(folder_2)
   for i in range(file_number): 
      file_path=os.path.join(folder,json_files[i])
      print(file_path)
      current_scene_verbs=json_verb_reader(file_path)
      for j in current_scene_verbs:
         action_count_list[j]+=1
            
            
def json_verb_reader(file):
   with open(file, 'r') as fcc_file:
      fcc_data = json.load(fcc_file)
#print(fcc_data)
   annotation_length=len(fcc_data['annotation'])
   verbs_in_szene=[]
   for i in range(annotation_length):
      if len(fcc_data['annotation'][0]['verb'])==1:
         verbs_in_szene.append(fcc_data['annotation'][i]['verb'][0])
      else:
         verbs_in_szene.append(fcc_data['annotation'][i]['verb'][0])
         verbs_in_szene.append(fcc_data['annotation'][i]['verb'][1])
   return verbs_in_szene
   
    
action_all_counter('/media/ziwei/yuankai/json_150_seperate')
print(action_count_list)

action_label=["idle","approach","leave","move","take","place","pour","cut","stir","wipe","drink","eat","wear","open","read","write","squeeze","smell","close","spray","prune","play","talk","peel","look at","comb","brush"]
df_verbs=pd.DataFrame(action_count_list,columns=['numbers'],index=action_label)

print(df_verbs.head())
df_verbs.sort_values(by=['numbers'],ascending=False, inplace=True)

#### changed 
print("")
print("The whole data frame is:")
print(df_verbs)
print("")
print()

####


#print(df_verbs.head(27))
df_verbs.plot(kind='bar', title='action distribution in videos')

plt.show()



