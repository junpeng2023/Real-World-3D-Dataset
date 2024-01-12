###


# statistics


## object_json_150.py 

```
#-- to plot the bar and donut diagram of objects in 150 videos

--dir_to_change:
1.
folder_path
2.
key
-- needs to change the title of the plots
e.g.
df_objects.plot(kind='bar', x='Object', y='Count', title='Object Distribution in 30 Videos')
plt.show()
df_objects['Count'].plot(kind='pie', labels=None, figsize=(8, 8), 
                         autopct=custom_autopct, startangle=90, pctdistance=0.85, wedgeprops=dict(width=0.3), 
                         title='Donut diagram of object distribution in 30 videos for training')

```


## object_json_30.py

```
#-- to plot the bar and donut diagram of objects in 30 validation videos

--dir_to_change:
1.
folder_path
2.
key
-- needs to change the title of the plots
e.g.
df_objects.plot(kind='bar', x='Object', y='Count', title='Object Distribution in 30 Videos')
plt.show()
df_objects['Count'].plot(kind='pie', labels=None, figsize=(8, 8), 
                         autopct=custom_autopct, startangle=90, pctdistance=0.85, wedgeprops=dict(width=0.3), 
                         title='Donut diagram of object distribution in 30 videos for training')

```
## object_json.py


```
#-- to plot the bar and donut diagram of objects in 120 training videos

--dir_to_change:
1.
folder_path
2.
key
-- needs to change the title of the plots
e.g.
df_objects.plot(kind='bar', x='Object', y='Count', title='Object Distribution in 30 Videos')
plt.show()
df_objects['Count'].plot(kind='pie', labels=None, figsize=(8, 8), 
                         autopct=custom_autopct, startangle=90, pctdistance=0.85, wedgeprops=dict(width=0.3), 
                         title='Donut diagram of object distribution in 30 videos for training')
```

## json_plot_20_val.py
```
#-- to plot the bar and donut diagram of actions in 150 videos

--dir_to_change:
1.
folder_path
2.
key
-- needs to change the title of the plots
e.g.
df_objects.plot(kind='bar', x='Object', y='Count', title='Object Distribution in 30 Videos')
plt.show()
df_objects['Count'].plot(kind='pie', labels=None, figsize=(8, 8), 
                         autopct=custom_autopct, startangle=90, pctdistance=0.85, wedgeprops=dict(width=0.3), 
                         title='Donut diagram of object distribution in 30 videos for training')
```


## json_plot_100_training.py
```
#-- to plot the bar and donut diagram of actions in 120 training videos

--dir_to_change:
1.
folder_path
2.
key
-- needs to change the title of the plots
e.g.
df_objects.plot(kind='bar', x='Object', y='Count', title='Object Distribution in 30 Videos')
plt.show()
df_objects['Count'].plot(kind='pie', labels=None, figsize=(8, 8), 
                         autopct=custom_autopct, startangle=90, pctdistance=0.85, wedgeprops=dict(width=0.3), 
                         title='Donut diagram of object distribution in 30 videos for training')
```



## json_plots.py

```
#-- to plot the bar and donut diagram of actions in 30 validation videos



--dir_to_change:
1.
folder_path
2.
key
-- needs to change the title of the plots
e.g.
df_objects.plot(kind='bar', x='Object', y='Count', title='Object Distribution in 30 Videos')
plt.show()
df_objects['Count'].plot(kind='pie', labels=None, figsize=(8, 8), 
                         autopct=custom_autopct, startangle=90, pctdistance=0.85, wedgeprops=dict(width=0.3), 
                         title='Donut diagram of object distribution in 30 videos for training')
```



# data integrity

## json_checker.py

```
#-- to check the integrity of objects and actions in json files

--dir_to_change:
1.
directory = <>
#-- directory with json files


```

## fps_calculator.py
```
#-- to calculate the fps of a video
--dir_to_change:
1.
video = cv2.VideoCapture(<video_directory>)


```

## average_frame.py
```
#-- to calculate average_frame among all videos



```

## action_counter.py

```
#-- to count the number of actions among json files



```

## max_frame.py

```
#-- to count the maximum frame among videos



```

## image resolution_cal.py

```
#-- to get the resolution of videos or frames


```

## size_calculator.py

```

```

