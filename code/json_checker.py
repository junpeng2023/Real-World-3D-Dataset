import json
import os

# List of all possible objects and actions
# objects = ["human1","human2","cup","milk","coffee","scoop","sugar","kettle","honey","bowl","tee bag","cereal","rag","glasses","pencil","notebook","newspaper","phone","flower","plants","container","shears","computer","ipad","place mat","bread","plate","knife","chopping block","apple","banana","peeler","mirror","comb","toothbrush","toothpaste","shaver"]
# actions = ["idle","approach","leave","move","take","place","pour","cut","stir","wipe","drink","eat","wear","open","read","write","squeeze","smell","close","spray","prune","play","talk","peel","comb","brush","shave"]

# # Initialize empty sets to store the objects and actions found in the json files
# found_objects = set()
# found_actions = set()

# # Path to the directory containing the json files
# directory = "/media/ziwei/yuankai/json_120"

# # Loop over all json files in the directory
# for folder in os.listdir(directory):
#     folder_directory = os.path.join(directory, folder)
#     for filename in os.listdir(folder_directory):
#         if filename.endswith(".json"):
#             with open(os.path.join(folder_directory, filename)) as f:
#                 data = json.load(f)
#                 for annotation in data['annotation']:
#                     found_objects.update(annotation['objects_all_string'])
#                     found_actions.update(annotation['verb'])

# # Check if all objects and actions were found in the json files
# missing_objects = set(objects) - found_objects
# missing_actions = set(actions) - found_actions

# print("Found objects:", found_objects)
# print("Found actions:", found_actions)

# print("Missing objects:", missing_objects)
# print("Missing actions:", missing_actions)

# List of all possible objects and actions
objects = ["human1","human2","cup","milk","coffee","scoop","sugar","kettle","honey","bowl","tee bag","cereal","rag","glasses","pencil","notebook","newspaper","phone","flower","plants","container","shears","computer","ipad","place mat","bread","plate","knife","chopping block","apple","banana","peeler","perfume","mirror","lipstick","cumb","hat","cloth","bag","keys","toothbrush","toothpaste","shaver"]
actions = ["idle","approach","leave","move","take","place","pour","cut","stir","wipe","drink","eat","wear","open","read","write","squeeze","smell","close","spray","prune","play","talk","peel","comb","brush","shave"]

actions_index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,20,21,22,23,24,25,26]


# Initialize empty sets to store the objects and actions found in the json files
found_objects = set()
found_actions = set()

# Path to the directory containing the json files
#directory = "/media/ziwei/yuankai/validation_20"

directory = "/media/ziwei/yuankai/json_val_30"

## for checking the training data
#directory = "/media/ziwei/yuankai/json_training_120"

# Loop over all json files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        with open(os.path.join(directory, filename)) as f:
            data = json.load(f)
            for annotation in data['annotation']:
                found_objects.update(annotation['objects_all_string'])
                found_actions.update(annotation['verb'])

# Check if all objects and actions were found in the json files
missing_objects = set(objects) - found_objects
missing_actions = set(actions_index) - found_actions

print("Found objects:", found_objects)
print("Found actions:", found_actions)

print("The number of found objects:", len(found_objects))
print("The number of found actions:", len(found_actions))

print("Missing objects:", missing_objects)
print("Missing actions:", missing_actions)


# print("Missing actions:", missing_actions)