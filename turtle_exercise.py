#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def turtle_movement():

    # start a new node
    rospy.init_node('cheer_turtle', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # define the required angle and speed(deg/sec)
    speed_angular = 3
    angle = 46.8

    # convert from angles to radians
    angular_speed = speed_angular*2*PI/360
    relative_angle = angle*2*PI/360

    # setting up angular_velocity
    vel_msg.angular.z = abs(angular_speed)

    #..
    t0 = rospy.Time.now().to_sec()

    # set initial angle to 0 before initiating the loop
    current_angle = 0

    # run the loop for rotating the turtle
    while(current_angle < relative_angle):
       
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0) # update the angle

    # set angular vel zero before setting up the linear motion of turtle
    vel_msg.angular.z = 0
    
    # define required distance and linear velocity
    speed_linear = 3
    distance= 4.3

    # setting up linear velocity
    vel_msg.linear.x = abs(speed_linear)
 
    while not rospy.is_shutdown():

        # ..
        t2 = rospy.Time.now().to_sec()

        # set initial distance to 0 before initiating the loop
        current_distance = 0

        # run the loop for linear movement of turtle
        while(current_distance < distance):
            
            velocity_publisher.publish(vel_msg)
            t3=rospy.Time.now().to_sec()
            current_distance= speed_linear*(t3-t2) # update the distance
       
        # set linear velocity to zero
        vel_msg.linear.x = 0

        # publish the final velocity (0) to stop the turtle
        velocity_publisher.publish(vel_msg)
    
    rospy.spin()

if __name__ == '__main__':
    try:
        turtle_movement()
    except rospy.ROSInterruptException:
        pass
