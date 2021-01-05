#!/usr/bin/env python

# control motors

from roboclaw import Roboclaw
import math

import rospy
from std_msgs.msg import Int32

#TODO: Tweak
meters_per_tick = 100
wheelbase = 100
#

# Init RoboClaw
address = 0x80
roboclaw = Roboclaw("/dev/ttyACM0", 38400)
roboclaw.Open()
roboclaw.ResetEncoders(address)
#

left_motor_speed = 0
right_motor_speed = 0
left_data = False
right_data = False

    
def update_motor():
    global left_data
    global right_data
    global left_motor_speed
    global right_motor_speed
    if(right_data and left_data):

    	if (left_motor_speed < 64): left_motor_speed -= 10
    	elif (left_motor_speed  > 64): left_motor_speed += 10

    	if (right_motor_speed < 64): right_motor_speed -= 10
    	elif (right_motor_speed  > 64): right_motor_speed += 10

    	roboclaw.ForwardBackwardM2(address,left_motor_speed)
    	roboclaw.ForwardBackwardM1(address,right_motor_speed)
    	print("right ", right_motor_speed, "left " , left_motor_speed)
	right_data = False
	left_data = False
	


def callback_left(data):
    global left_data
    global right_data
    global left_motor_speed
    global right_motor_speed
    left_motor_speed = (-1* int(data.data)) +64 
    left_data = True
    update_motor()
    #left_motor_speed = left_motor_speed * 20/3000
    # left_motor_speed += 64
    #print("leftMotor " , left_motor_speed)
    print("leftMotor original" , data.data)
def callback_right(data):
    global left_data
    global right_data
    global left_motor_speed
    global right_motor_speed
    right_motor_speed = (-1*int(data.data))  +64
    right_data = True
    update_motor()
    #right_motor_speed = right_motor_speed * 20/3000
    # right_motor_speed += 64
    #print("rightMotor " , right_motor_speed)
    print("rightMotor original" , data.data)

def listener():
    print("listen")
    rospy.init_node('motor_controller', anonymous = False)

    rospy.Subscriber("lwheel_desired_rate", Int32, callback_left)
    rospy.Subscriber("rwheel_desired_rate", Int32, callback_right)

    rospy.spin()

if __name__ == '__main__':
    listener()


