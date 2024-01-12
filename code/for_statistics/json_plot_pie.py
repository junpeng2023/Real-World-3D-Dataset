import json
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt


action_count=[35884, 14449, 10180, 3763, 21695, 18793, 6050, 2051, 3117, 558, 3462, 3006, 186, 1477, 7483, 4673, 636, 530, 610, 2070, 2126, 2755, 1941, 2137, 1605, 1934, 3393]
action_label=["idle","approach","leave","move","take","place","pour","cut","stir","wipe","drink","eat","wear","open","read","write","squeeze","smell","close","spray","prune","play","talk","peel","comb","brush","shave"]
object_label=["human1","human2","cup","milk","coffee","scoop","sugar","kettle","honey","bowl","tee bag","cereal","rag","glasses","pencil","notebook","newspaper","phone","flower","plants","container","shears","computer","ipad","place mat","bread","plate","knife","chopping block","apple","banana","peeler","mirror","comb","toothbrush","toothpaste","shaver"]
df_verbs=pd.DataFrame(action_count,columns=['numbers'],index=action_label)

print("The number of found actions:", len(action_count))
#   df_verbs.plot(kind='bar', title='action distribution in videos')    

print(df_verbs.head())
print(df_verbs.columns)
df_verbs = df_verbs.rename(columns={"actions": "numbers"})

df_verbs.sort_values(by=['numbers'],ascending=False, inplace=True)
df_verbs.reset_index(inplace=True)
df_verbs = df_verbs.rename(columns={"index": "Action Types", "numbers": "Actions"})
# df_verbs['percentage'] = df_verbs['Actions']/df_verbs['Actions'].sum() * 100

# # create a mask for percentage values greater than or equal to 4
# mask = df_verbs['percentage'] >= 4

# # create new labels column
# df_verbs['labels'] = df_verbs['Action Types']

# # set labels for percentage values less than 4 to empty string
# df_verbs.loc[~mask, 'labels'] = ''

print(df_verbs)

#print(df_verbs.head(27))


df_verbs['custom_labels'] = df_verbs.apply(lambda row: '' if row['Actions'] < 0.01 else row['Action Types'], axis=1)

def custom_autopct(pct):
    return ('%1.1f%%' % pct) if pct > 2 else ''

df_verbs['Actions'].plot(kind='pie', labels=None, figsize=(8, 8), 
                         autopct=custom_autopct, startangle=90, pctdistance=0.85, 
                         title='The pie diagram of action distribution in videos')


plt.legend(labels=df_verbs['Action Types'], loc='center right',bbox_to_anchor=(1.25, 0.5))

plt.show()
df_verbs.plot(kind='bar', title='action distribution in videos')
plt.show()
# read the json file        
hoi=[[12823, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [23061, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2553, 1925, 966, 3193, 3678, 0, 0, 0, 0, 3462, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 721, 393, 102, 1109, 704, 1611, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 524, 352, 137, 545, 599, 1038, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 697, 535, 98, 944, 901, 0, 0, 3023, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 386, 192, 145, 436, 445, 524, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 885, 375, 414, 1243, 1142, 1989, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 61, 0, 0, 141, 183, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 224, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 589, 450, 663, 511, 562, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 328, 240, 108, 708, 577, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 444, 300, 117, 706, 508, 888, 0, 94, 0, 0, 711, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 139, 110, 49, 348, 249, 0, 0, 0, 558, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 287, 166, 34, 635, 33, 0, 0, 0, 0, 0, 0, 186, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 518, 395, 13, 1094, 485, 0, 0, 0, 0, 0, 0, 0, 0, 0, 99, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 355, 382, 111, 543, 315, 0, 0, 0, 0, 0, 0, 0, 792, 1584, 4161, 0, 0, 313, 0, 0, 0, 0, 0, 0, 0, 0], [0, 326, 153, 36, 1009, 363, 0, 0, 0, 0, 0, 0, 0, 685, 3134, 413, 0, 0, 297, 0, 0, 0, 0, 0, 0, 0, 0], [0, 236, 201, 0, 431, 414, 0, 0, 0, 0, 0, 0, 0, 0, 325, 0, 0, 0, 0, 0, 0, 100, 1941, 0, 0, 0, 0], [0, 435, 301, 21, 1039, 830, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 452, 0, 1081, 842, 0, 0, 0, 0, 0, 0], [0, 221, 190, 112, 369, 296, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 78, 0, 989, 1284, 0, 0, 0, 0, 0, 0], [0, 354, 492, 10, 573, 581, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 470, 320, 126, 710, 802, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 335, 133, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1687, 0, 0, 0, 0, 0, 0, 2556, 0, 0, 0, 0, 0], [0, 99, 103, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 753, 0, 0, 0, 0, 0, 0, 99, 0, 0, 0, 0, 0], [0, 45, 89, 49, 121, 37, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 172, 133, 0, 220, 542, 0, 0, 0, 0, 0, 732, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 232, 169, 68, 490, 354, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 311, 175, 0, 339, 513, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 271, 141, 223, 152, 187, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 260, 210, 34, 610, 674, 0, 981, 0, 0, 0, 1030, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1056, 0, 0, 0], [0, 522, 215, 28, 550, 518, 0, 1070, 0, 0, 0, 533, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 532, 0, 0, 0], [0, 183, 164, 14, 314, 273, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 549, 0, 0, 0], [0, 465, 329, 69, 735, 438, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 267, 230, 0, 515, 365, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 44, 0, 0, 0, 0, 0, 0, 0, 1605, 0, 0], [0, 301, 252, 16, 578, 488, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1934, 0], [0, 220, 175, 0, 374, 331, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 368, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 237, 190, 0, 410, 406, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3393]]

df_hoi=pd.DataFrame(hoi)

print(df_hoi.columns)

df_hoi.index=object_label

df_hoi.columns=action_label



print(df_hoi)


# Write the DataFrame to an Excel file
writer = pd.ExcelWriter('hoi_statistic.xlsx', engine='xlsxwriter')
df_hoi.to_excel(writer)
writer.save()



print('DataFrame output to Excel successfully!')     

# # Plot the DataFrame
# df_hoi.plot(kind='bar', stacked=True, figsize=(20, 10)) # Stacked bar chart
# plt.title('HOI statistic')  # Add a title to the plot
# plt.xlabel('Object')  # Add x-axis label
# plt.ylabel('Action')  # Add y-axis label
# plt.legend(loc='upper right')  # Add a legend




    


plt.show()
