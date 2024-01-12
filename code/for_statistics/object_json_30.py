##
##
####
import json
import os
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

def json_object_reader(file, key):
    with open(file, 'r') as fcc_file:
        fcc_data = json.load(fcc_file)

    object_counts = Counter()
    for annotation in fcc_data['annotation']:
        objects = annotation[key]
        object_counts.update(objects)

    return object_counts

def aggregate_object_counts(folder, key):
    total_counts = Counter()
    json_files = [f for f in os.listdir(folder) if f.endswith('.json')]
    json_files.sort(key=lambda x: int(x.split('_')[0]))

    for json_file in json_files:
        file_path = os.path.join(folder, json_file)
        counts = json_object_reader(file_path, key)
        total_counts.update(counts)

    return total_counts

# Example Usage
folder_path = '/media/ziwei/yuankai/json_val_30'  # Update this to your folder path
key = 'objects_all_string'  # or 'objects_all_num'

object_counts = aggregate_object_counts(folder_path, key)
print(object_counts)

# Converting to DataFrame for better visualization
df_objects = pd.DataFrame(object_counts.items(), columns=['Object', 'Count'])
df_objects.sort_values(by='Count', ascending=False, inplace=True)

print(df_objects.head())

print(df_objects)


def custom_autopct(pct):
    return ('%1.1f%%' % pct) if pct > 2 else ''
# Plotting
df_objects.plot(kind='bar', x='Object', y='Count', title='Object Distribution in 30 Videos')
plt.show()
df_objects['Count'].plot(kind='pie', labels=None, figsize=(8, 8), 
                         autopct=custom_autopct, startangle=90, pctdistance=0.85, wedgeprops=dict(width=0.3), 
                         title='Donut diagram of object distribution in 30 videos for training')
plt.legend(labels=df_objects['Object'], loc='center right',bbox_to_anchor=(1.25, 0.5))

plt.show()
