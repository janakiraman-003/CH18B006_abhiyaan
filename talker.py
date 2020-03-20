#!/usr/bin/env python


import rospy
from std_msgs.msg import String

def talker():

    # start the new node
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)

    # runs the loop 10 times per second
    rate = rospy.Rate(10) # 10hz

    # run the loop for printing the message
    while not rospy.is_shutdown():
        hello_str = "welcome to Abhiyaan %s" % rospy.get_time()
        rospy.loginfo(hello_str)

        # publishes the message
        pub.publish(hello_str)

        # exits the loop after definite amount of time
        rate.sleep()

if __name__ == '__main__':
    
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
