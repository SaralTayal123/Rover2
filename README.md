# Rover2
Updated version of my personal assistant robot. This time with ROS, and a slew of new sensors and updated functionality!

### How to launch:
`./launch.sh`


### Setup Requirements:
* Raspberry Pi running ROS Melodic. I used the prebuilt image from: https://husarion.com/downloads/  
* Build Cartographer from source: https://google-cartographer-ros.readthedocs.io/en/latest/compilation.html  
* Before running the final make command, refer to this link to fix mapping: https://github.com/cartographer-project/cartographer/issues/1498  
* git clone this project  
* run through the YDLidar setup (https://github.com/EAIBOT/ydlidar)  
* `cd Rover2`  
* `catkin_make` (Only needs to be done the first time)  
* `chmod +x ./launch.sh` (Permissions for the custom launch script. Only needs to be done the first time)  

### Credits:
* Ubiquity for prebuilt image
* Gbot for the cartographer integration template
* Differential drive stuff

### Working list of tweaks to document in final ReadMe:
1. Wack ydlidar tf tree and how I fixed that
2. Really absurd bug in the ydlidar driver where the `/scan` messages' second's field uses nanoseconds instead of seconds (TODO: link fix)
3. Cartographer's probability rating for maps is great but doesn't play well with ros_navigation. Fix through change in driver before building from source
4. How to setup custom RViz windows (to visualise paths/costmaps)
5. Issues with AMCL- YOLO and use hack-y localisation from SLAM to generate `robot_pose` msg
6. Ros_navigation doesn't play well with dynamic maps. They want static maps after SLAM is done. That's boring. Fix by using sliding windows on global cost map centered at /odom. Fix local mapping by switching to teb_local_planner
7. Install xterm (for tabs)
8. How to modify launch script
9. Remove devel and build folder
10. Source cartographer after install if you want your catkin_make to work
11. sudo apt-get install teb...
