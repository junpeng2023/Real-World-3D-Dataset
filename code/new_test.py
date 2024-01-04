import json
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

action_count_list= [0] *27
print(action_count_list)

def json_verb_reader(file):
    with open(file, 'r') as fcc_file:
        fcc_data = json.load(fcc_file)
#print(fcc_data)    
    annotation_length=len(fcc_data['annotation'])
    
    if annotation_length == 0:
        return []
    elif annotation_length== 1:
        return fcc_data['annotation'][0]['verb']