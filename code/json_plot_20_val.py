import json
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
action_count_list = [0] * 27
print(action_count_list)


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


def action_all_counter(folder):
   json_files=[]
   for f in os.listdir(folder):
      if f.endswith('.json'):
         json_files.append(f)
   json_files.sort(key=lambda x:int(x[0:3]))
   file_number=len(json_files)
   #### changed
   print("The file numbers are:")
   print(file_number)
   ####
   
   for i in range(file_number):
      file_path=os.path.join(folder,json_files[i])
      current_scene_verbs=json_verb_reader(file_path)
      for j in current_scene_verbs:
         action_count_list[j]+=1
   
    
action_all_counter('/media/ziwei/yuankai/json_val_30')
print(action_count_list)

action_label=["idle","approach","leave","move","take","place","pour","cut","stir","wipe","drink","eat","wear","open","read","write","squeeze","smell","close","spray","prune","play","talk","peel","comb","brush","shave"]
df_verbs=pd.DataFrame(action_count_list,columns=['numbers'],index=action_label)

print(df_verbs.head())
df_verbs.sort_values(by=['numbers'],ascending=False, inplace=True)
df_verbs.reset_index(inplace=True)
df_verbs = df_verbs.rename(columns={"index": "Action Types", "numbers": "Actions"})
print(df_verbs.head())

#### changed 
print("")
print("The whole data frame is:")
print(df_verbs)
print("")
print()

####
df_verbs['custom_labels'] = df_verbs.apply(lambda row: '' if row['Actions'] < 0.01 else row['Action Types'], axis=1)

def custom_autopct(pct):
    return ('%1.1f%%' % pct) if pct > 2 else ''

#print(df_verbs.head(27))
df_verbs.plot(kind='bar', title='action distribution in 30 videos for validation')
plt.show()

df_verbs['Actions'].plot(kind='pie', labels=None, figsize=(8, 8), 
                         autopct=custom_autopct, startangle=90, pctdistance=0.85, wedgeprops=dict(width=0.3), 
                         title='Donut diagram of action distribution in 30 videos for validation')


plt.legend(labels=df_verbs['Action Types'], loc='center right',bbox_to_anchor=(1.25, 0.5))

plt.show()
