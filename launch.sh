#!/bin/sh

# This script launches all the relavent ROS nodes in new tabls and helps the sourcing process.

# Launch Lidar
xterm -title "App 1" -e "source devel/setup.bash && roslaunch ydlidar lidar.launch" &
# lxterminal --command 'cd ~/slam2 && source devel/setup.bash && roslaunch ydlidar lidar.launch'

# Wait a couple of seconds for the lidar to fire up
sleep 5

# Launch SLAM
xterm -title "App 2" -e "source devel/setup.bash && roslaunch slam slam.launch" &
# lxterminal --command 'cd ~/slam2 && source devel/setup.bash && roslaunch slam slam.launch'

# Launch Navigation (local + global costmaps & planning)
xterm -title "App 3" -e "source devel/setup.bash && roslaunch rover2_2dnav move_base.launch" &
# lxterminal --command 'cd ~/slam2 && source devel/setup.bash && roslaunch rover2_2dnav move_base.launch'

# Launch Robot Pose Generator 
xterm -title "App 4" -e "source devel/setup.bash && rosrun robot_pose_publisher robot_pose_publisher" 
# lxterminal --command 'cd ~/slam2 && source devel/setup.bash && rosrun robot_pose_publisher robot_pose_publisher'

# Launch Motor controller and differential drive converter
