#!/usr/bin/env python

# TODO ensure that python/3

# Calculate Odom information for differential drive 
# https://www.cs.cmu.edu/~16311/s07/labs/NXTLabs/Lab%203.html

from roboclaw import Roboclaw
import math

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

rospy.init_node('odometry_publisher')

odom_pub = rospy.Publisher("odom", Odometry, queue_size=50)
odom_broadcaster = tf.TransformBroadcaster()

#TODO: Tweak
meters_per_tick = 100
wheelbase = 100
#

x = 0.0
y = 0.0
th = 0.0

vx = 0.0
vy = 0.0
vth = 0.0

current_time = rospy.Time.now()
last_time = rospy.Time.now()

r = rospy.Rate(1)

# Init RoboClaw
address = 0x80
roboclaw = Roboclaw("/dev/ttyACM0", 38400)
roboclaw.Open()
roboclaw.ResetEncoders(address)
#

_, old_encoder_1, _ = roboclaw.ReadEncM1(address)
_, old_encoder_2, _ = roboclaw.ReadEncM2(address)

while not rospy.is_shutdown():
    current_time = rospy.Time.now()

    # TODO experiment with roboclaw native speed calcualtion
    # Going to do manual for now for consistancy. 

    _, encoder_1, _ = roboclaw.ReadEncM1(address)
    _, encoder_2, _ = roboclaw.ReadEncM2(address)

    dt = (current_time - last_time).to_sec()
    
    V_left = ((encoder_1 - old_encoder_1)/dt) * meters_per_tick 
    V_right = ((encoder_2 - old_encoder_2)/dt) * meters_per_tick 
    
    ###
    velocity = (V_left + V_right) / 2
    omega = (V_right - V_left ) / wheelbase
    ###


    ###
    k00 = velocity * math.cos(th)
    k01 = velocity * math.sin(th)
    k02 = omega

    k10 = velocity * math.cos(th + ((dt/2) * k02))
    k11 = velocity * math.sin(th + ((dt/2) * k02))
    k12 = omega

    k20 = velocity * math.cos(th + ((dt/2) * k12))
    k21 = velocity * math.sin(th + ((dt/2) * k12))
    k22 = omega 

    k30 = velocity * math.cos(th + ((dt/2) * k22))
    k31 = velocity * math.sin(th + ((dt/2) * k22))
    k32 = omega 

    delta_x = (dt/6) * (k00 + (2*(k10 + k20)) + k30)
    delta_y = (dt/6) * (k01 + (2*(k11 + k21)) + k31)
    delta_th = dt * omega

    vx = delta_x/dt
    vy = delta_y/dt
    vth = delta_th/dt

    ###

    x = x + delta_x
    y = y + delta_y
    th = th + delta_th 
    
    # since all odometry is 6DOF we'll need a quaternion created from yaw
    odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)

    # first, we'll publish the transform over tf
    odom_broadcaster.sendTransform(
        (x, y, 0.),
        odom_quat,
        current_time,
        "base_link",
        "odom"
    )

    # next, we'll publish the odometry message over ROS
    odom = Odometry()
    odom.header.stamp = current_time
    odom.header.frame_id = "odom"

    # set the position
    odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))

    # set the velocity
    odom.child_frame_id = "base_link"
    odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))

    # publish the message
    odom_pub.publish(odom)

    last_time = current_time
    r.sleep()

    old_encoder_1 = encoder_1
    old_encoder_2 = encoder_2
