#! /usr/bin/env python
import math
import numpy
import rospy
import tf2_py as tf2
import tf2_ros
from nav_msgs.msg import Odometry
from std_msgs.msg import Header
from gazebo_msgs.srv import GetModelState, GetModelStateRequest
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

rospy.init_node('odom_pub')

odom_pub=rospy.Publisher ('/odom_status', Odometry, queue_size=50)

rospy.wait_for_service ('/gazebo/get_model_state')
get_model_srv = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)

odom = Odometry()
header = Header()
header.frame_id ='/odom'

model = GetModelStateRequest()
model.model_name='carbot'

r = rospy.Rate(2)

while not rospy.is_shutdown():
    result = get_model_srv(model)

    odom.pose.pose = result.pose
    odom.twist.twist = result.twist
    header.stamp = rospy.Time.now()
    odom.header = header

    odom_pub.publish (odom)

    r.sleep()
