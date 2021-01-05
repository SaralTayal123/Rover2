#!/bin/sh

# This script launches all the relavent ROS nodes in new tabls and helps the sourcing process.

# Launch Lidar
xterm -title "App 1" -hold -e "source devel/setup.bash && roslaunch ydlidar lidar.launch" &
# lxterminal --command 'cd ~/slam2 && source devel/setup.bash && roslaunch ydlidar lidar.launch'

# Wait a couple of seconds
 sleep 6

# Launch SLAM
xterm -title "App 2" -hold -e "source devel/setup.bash && roslaunch slam slam.launch" &
# lxterminal --command 'cd ~/slam2 && source devel/setup.bash && roslaunch slam slam.launch'

# Launch Navigation (local + global costmaps & planning)
xterm -title "App 3" -hold -e "source devel/setup.bash && roslaunch rover2_2dnav move_base.launch" &
# lxterminal --command 'cd ~/slam2 && source devel/setup.bash && roslaunch rover2_2dnav move_base.launch'

# Launch Robot Pose Generator 
xterm -title "App 4" -hold -e "source devel/setup.bash && rosrun robot_pose_publisher robot_pose_publisher" &
# lxterminal --command 'cd ~/slam2 && source devel/setup.bash && rosrun robot_pose_publisher robot_pose_publisher'


# Launch Camera
xterm -title "App 5" -hold -e "source devel/setup.bash && roslaunch video_stream_opencv camera.launch" &

# Launch Diff_drive Controller 
xterm -title "App 6" -hold -e "source devel/setup.bash && roslaunch diff_drive demo.launch " & 

# Launch Motor Controller 
xterm -title "App 7" -hold -e "source devel/setup.bash && rosrun roboclaw motor.py " 
