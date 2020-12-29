#!/bin/sh

# This script launches all the relavent ROS nodes in new tabls and helps the sourcing process.

# Launch Lidar
lxterminal --command 'cd ~/slam2 && source devel/setup.bash && roslaunch ydlidar lidar.launch'
# Wait a couple of seconds
sleep 3
# Launch SLAM
lxterminal --command 'cd ~/slam2 && source devel/setup.bash && roslaunch slam slam.launch'
# Launch Navigation (local + global costmaps & planning)
lxterminal --command 'cd ~/slam2 && source devel/setup.bash && roslaunch rover2_2dnav move_base.launch'
# Launch Robot Pose Generator 
lxterminal --command 'cd ~/slam2 && source devel/setup.bash && rosrun robot_pose_publisher robot_pose_publisher'
# Launch Motor controller and differential drive converter
