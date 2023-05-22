

## A Real world 3D Dataset for Human-Robot Interaction 


## Description
This dataset is a collection of 120 RGB-D videos, The 120 videos consist of 10 different scenarios,namely ”working”, ”flower”, ”coffee” and so on. all of which are designed to simulate the elderly's daily life under laboratory condition.T Each scene has three modes:
”single person”, ”multi person” and ”cooperation”. There are five completely random action sequence videos in each mode. Compare to other existing state-of-the-art datasets,for the same scenario, We recorded not only the actions of a single person, but, also recorded the collaboration between the two people,in order to improve the performance of humanoid robots.




## Dataset in number
Some facts about the Dataset.

<table>
	<tr>
	    <td >Subjects</td>
	    <td >8 subjects (2 female,6 male; 7 right-handed, 1 left-handed)</td>
	</tr>
	<tr>
	    <td >Senarios</td>
	    <td >coffee/breakfast/reading/flower/working/eating/fruit/make_up/wear/bad</td>
	</tr>
	<tr>
	    <td >Recordings</td>
	    <td >120 RGB-D videos(we record 3 groups(with 5 repetitions) videos for each senario)</td>
	</tr>
    <tr>
	    <td >Playtime</td>
	    <td >2 hours and 18 minutes, or 221 000 RGB-D image frames</td>
	</tr>
    <tr>
	    <td >Quality</td>
	    <td >640 px × 480 px image resolution; 30 fps</td>
	</tr>
    <tr>
	    <td >Actions</td>
	    <td >27 primary actions </td>
	</tr>
     <tr>
	    <td >Objects</td>
	    <td >40 commonly used objects in daily life </td>
	</tr>
     <tr>
	    <td >Annotations</td>
	    <td >Actions fully labelled for both hands individually; 5413 frames labelled with object bounding boxes</td>
	</tr>
    
    



</table>


## Action Label Mapping
Refer to the following table for a mapping of action label IDs and their symbolic name.

<table>
	<tr>
	    <th>#</th>
	    <th>Action</th>
	    <th>Description</th>  
	</tr >
	<tr >
	    <td>0</td>
	    <td>idle</td>
	    <td>The human does nothing semantically meaningful.</td>
	</tr>
	<tr>
        <td>1</td>
	    <td>approach</td>
	    <td>The human approaches an object wgich is going to be relevant.</td>
	</tr>
	<tr>
	    <td >2</td>
	    <td>leave</td>
	    <td>The human leaves from an object after interacting with it.</td>
	</tr>
    <tr>
    <td >3</td>
	    <td >move</td>
	    <td >The human changes the placement of an object.</td>
	<tr>
	    <td >4</td>
	    <td >take </td>
	    <td >The human holds an object to get ready to use it.</td>
	</tr>
	<tr>
	    <td >5</td>
	    <td >place</td>
	    <td >The human places an object after using it.</td>
	</tr>
	<tr>
	    <td >6</td>
	    <td >pour</td>
	    <td >The human pours something from the grasped object.</td>
	</tr>
	<tr>
	    <td >7</td>
	    <td >cut</td>
	    <td >The human cuts something with the grasped object.</td>
	</tr>
    <tr>
	    <td >8</td>
	    <td >stir</td>
	    <td >The human stirs something with the grasped object.</td>
	</tr>
    <tr>
	    <td >9</td>
	    <td >wipe</td>
	    <td >The human wipes something with the grasped object.</td>
	</tr>
    <tr>
	    <td >10</td>
	    <td >drink</td>
	    <td >The human drinks something.</td>
	</tr>
    <tr>
	    <td >11</td>
	    <td >eat</td>
	    <td >The human eats something.</td>
	</tr>
    <tr>
	    <td >12</td>
	    <td >wear</td>
	    <td >The human wears the object on the body.</td>
	</tr>
    <tr>
	    <td >13</td>
	    <td >open</td>
	    <td >The human opens an object by hands.</td>
	</tr>
    <tr>
	    <td >14</td>
	    <td >read</td>
	    <td >The human reads an object in hand.</td>
	</tr>
    <tr>
	    <td >15</td>
	    <td >write</td>
	    <td >The human wirtes with the grasped object.</td>
	</tr>
    <tr>
	    <td >16</td>
	    <td >squeeze</td>
	    <td >The human squeeze something by hand.</td>
	</tr>
    <tr>
	    <td >17</td>
	    <td >smell</td>
	    <td >The human smell something.</td>
	</tr>
    <tr>
	    <td >18</td>
	    <td >close</td>
	    <td >The human closes something by hand.</td>
	</tr>
    <tr>
	    <td >19</td>
	    <td >spray</td>
	    <td >The human spray something by hand.</td>
	</tr>
    <tr>
	    <td >20</td>
	    <td >prune</td>
	    <td >The human prunes plants with sheers.</td>
	</tr>
    <tr>
	    <td >21</td>
	    <td >play</td>
	    <td >The human operate on computer or phone.</td>
	</tr>
    <tr>
	    <td >22</td>
	    <td >talk</td>
	    <td >The human speak on a phone.</td>
	</tr>
    <tr>
	    <td >23</td>
	    <td >peel</td>
	    <td >The human peels fruits with peeler.</td>
	</tr>
    <tr>
	    <td >24</td>
	    <td >look at</td>
	    <td >The human looks at something.</td>
	</tr>
     <tr>
	    <td >25</td>
	    <td >cumb</td>
	    <td >The human cumb the hair.</td>
	</tr>
     <tr>
	    <td >26</td>
	    <td >brush</td>
	    <td >The human brushes something with hand.</td>
	</tr>
</table>

## Object Class Label Mapping
Refer to the following table for a mapping of object class label IDs and their symbolic name.

|   #   | object  |  #  |  Object | #  |  Object |#  |  Object |
|  :----: | :----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0  | human1  |11  | cereal    |22  | computer       |33  | mirror |
| 1  | human2  |12  | rug       |23  | ipad           |34  | lipstick |
| 2  | cup     |13  | glasses   |24  | place mat      |35  | cumb |
| 3  | milk    |14  | pencil    |25  | bread          |36  | hut |
| 4  | coffee  |15  | notebook  |26  | plate          |37  | cloth |
| 5  | scoop   |16  | newspaper |27  | knife          |38  | bag |
| 6  | sugar   |17  | phone     |28  | chopping block |39  | keys |
| 7  | kettle  |18  | flower    |29  | apple          |40  |toothbrush|
| 8  | honig   |19  | plants    |30  | banana         |41  |toothpaste|
| 9  | bowl    |20  | container |31  | peeler|
| 10 |tee bag  |21  | shears    |32  | perfume|


## Action Ground Truth

<p>&nbsp;</p>
    <p>For each video human action grundtruth, we record the start and end frames of each action
		as follows, and then represent the human action and the object being touched with the
		corresponding numeric code in the middle bracket. For example, [1,17] means that the
		person approaches the phone. The action segment[...94,[22,17],263...] means the human is
		talking on a phone from frame 94 to frame 263.
		For multiple people mode as well as for cooperative mode. The actions of each person
		in the scene are labelled in turn in the middle brackets. For example, the action segment
		[21,17,5,2] means that the first person is playing with his phone while the second person
		is putting down his glass.</p>
	<div style="width:75%; margin:auto;" align="left">
	
		<figure style="text-align:center;">
		<pre style="background-color: #d7d8d8d8; padding: 10px;">
        work_single_2:[0,[0,0],42,[1,22],53,[21,22],189,[2,22],196,[1,14],206,[4,14],210,[1,15],221,[13,15]<br>,262,[15,15],463,[18,15],480,[5,14],507,[2,14],547,[0,0],564]
		</pre>
		<figcaption style="text-align:center;">Sample of action grundtruth template for single person mode</figcaption>
		</figure>
		</div>

	<div style="width:75%; margin:auto;" align="left">
	
		<figure style="text-align:left;">
		<pre style="background-color: #d7d8d8d8; padding: 10px;">
        coffee_mp_4:[0,[0,0,0,1],11,[1,2,0,1],37,[1,2,1,2],40,[4,2,1,2]<br>,42,[4,2,4,2],64,[5,2,5,2],66,[5,2,1,5],71,[5,2,4,5],75,[2,2,8,5],83,[1,4,2,2],96,[1,4,1,2],101,[4,4,8,5],123,[6,4,8,5]
		,135,[6,4,5,5],140,[6,4,2,5],151,[6,4,1,3],161,[6,4,4,3],181,[3,4,4,3]<br>,196,[5,4,5,3],200,[5,4,2,3],211,[5,4,1,4],215,[6,4,1,4]],222,[2,4,4,4],232,[1,7,4,4],236,[1,7,5,4]
		,261,[4,7,4,4],273,[4,7,6,4],307,[6,7,5,4],334,[6,7,2,4],347,[6,7,1,5]<br>,357,[5,7,4,5],368,[5,7,2,5],378,[2,7,2,5],386,[2,7,1,7],399,[1,6,4,7],413,[1,3,4,7],424,[4,3,6,7]
		,456,[6,3,6,7],475,[6,3,5,2],503,[5,3,3,7],523,[5,2,5,7],537,[2,3,5,7]<br>,544,[1,2,2,7],557,[4,5,2,7],568,[8,5,4,5],576,[8,5,8,5],615,[8,5,5,5],617,[8,5,2,2],627,[8,5,1,6]
		,634,[5,5,1,6],641,[2,5,4,6],655,[1,3,4,6],664,[4,3,4,6],679,[4,3,6,6]<br>,685,[5,3,6,6],700,[2,3,6,6],717,[1,2,4,6],721,[1,2,5,6],732,[4,2,5,6],741,[5,2,5,6],747,[5,2,2,6]
		,758,[2,2,8,5],776,[0,0,8,5],795,[0,0,5,5],810,[0,0,2,5],819,[0,0,1,3]<br>,825,[0,0,3,3],837,[0,0,2,3],843,[0,0,1,3],846,[0,0,4,3],856,[0,0,6,3],881,[0,0,4,3],897,[0,0,5,3]
		,912,[0,0,2,3],921,[0,0,1,5],928,[0,0,4,5],935,[0,0,8,5],966,[0,0,5,5]<br>,970,[0,0,2,5],992,[0,0,4,2],1006,[0,0,10,2],1025,[0,0,5,2],1052,[0,0,2,2],1062,[0,0,0,1],1085]
		</pre>
		<figcaption style="text-align:center;">Sample of action grundtruth template for multi person mode</figcaption>
		</figure>
		</div>

	<div style="width:75%; margin:auto;" align="left">
	
		<figure style="text-align:left;">
		<pre style="background-color: #d7d8d8d8; padding: 10px;">
        work_col_2:[0,[0,0,0,1],24,[1,22,0,1],34,[21,22,0,1],115,[21,22,1,17]<br>,124,[14,22,1,17],145,[14,22,4,17],166,[1,17,5,17],182,[4,17,2,17],200,[4,17,0,1],211,[22,17,0,1],365,[22,17,1,2]
		,392,[22,17,4,2],412,[5,17,5,2],432,[2,17,5,2],437,[1,2,2,2],463,[4,2,0,1]<br>,490,[10,2,0,1],555,[5,2,0,1],586,[2,2,0,1],603,[0,0,0,1]
		,613,[0,0,1,2],644,[0,0,3,2],677,[0,0,2,2],697,[0,0,0,1],725]
		</pre>
		<figcaption style="text-align:center;">Sample of action grundtruth template for collabration mode</figcaption>
		</figure>
		</div>
## RGB-D Camera Setup

We use Intel RealSense Depth Camera D435i as RGB-D camera to record data.The Intel® RealSense™ D435i places an IMU into our cutting‑edge stereo depth camera. With an Intel module and vision processor in a small form factor, the D435i is a powerful  complete package which can be paired with customizable software for a depth camera that is capable of understanding it's own movement.

## Guidline to Data recording

 ```
 
 
 roscore

 roslaunch realsense2_camera rs_camera.launch align_depth:=true depth_width:=640 depth_height:=480 depth_fps:=30 color_width:=640 color_height:=480 color_fps:=30 


rosbag record /camera/accel/imu_info /camera/accel/sample /camera/align_to_color/parameter_descriptions /camera/align_to_color/parameter_updates /camera/aligned_depth_to_color/camera_info /camera/aligned_depth_to_color/image_raw /camera/color/camera_info /camera/color/image_raw/compressed /camera/extrinsics/depth_to_color /camera/extrinsics/depth_to_infra1 /tf /tf_static -o breakfast.bag


```




## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
