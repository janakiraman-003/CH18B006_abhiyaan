#!/usr/bin/env python


import rospy
from std_msgs.msg import String

def callback(data):

    # prints the received message
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener():

    # initiates the node
    rospy.init_node('listener', anonymous=True)

    # subscribes to the relevant topic
    rospy.Subscriber('chatter', String, callback)

    # spin() simply keeps python from exiting until this node is stopped manualy
    rospy.spin()

if __name__ == '__main__':

    listener()
