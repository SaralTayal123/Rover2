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

def callback_left(data):
    left_motor_speed = int(data.data)
    left_motor_speed = left_motor_speed * 20/3000
    # left_motor_speed += 64
    roboclaw.ForwardM1(address,left_motor_speed)
    print("leftMotor " , left_motor_speed)
    print("leftMotor original" , data.data)
def callback_right(data):
    right_motor_speed = int(data.data)
    right_motor_speed = right_motor_speed * 20/3000
    # right_motor_speed += 64
    roboclaw.ForwardM2(address,right_motor_speed)
    print("rightMotor " , right_motor_speed)
    print("rightMotor original" , data.data)

def listener():
    print("listen")
    rospy.init_node('motor_controller', anonymous = False)

    rospy.Subscriber("lwheel_desired_rate", Int32, callback_left)
    rospy.Subscriber("rwheel_desired_rate", Int32, callback_right)

    rospy.spin()

if __name__ == '__main__':
    listener()


