#!/usr/bin/env python3
# Import ROS libraries and messages
import rospy
from sensor_msgs.msg import Image
import test
from test import *
# Import OpenCV libraries and tools
import cv2
from cv_bridge import CvBridge, CvBridgeError
import traceback


# Initialize the ROS Node named 'opencv_example', allow multiple nodes to be run with this name
rospy.init_node('opencv_example', anonymous=True)


# Initialize the CvBridge class
bridge = CvBridge()

# Define a callback for the Image message
def image_callback(img_msg):

    # Try to convert the ROS Image message to a CV2 Image
    try:
      cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")[:,:,:3]
      # img_path2=r'/home/iitdautomation/DLive/PINet/dataset/Test_images/11A00148.JPG'
      # cv_image = cv2.imread(img_path2)
      print("hit")
      run_lane_detect(cv_image)
    except Exception:
      print(traceback.format_exc())



# Initalize a subscriber to the "/camera/rgb/image_raw" topic with the function "image_callback" as a callback
sub_image = rospy.Subscriber("/zed2/zed_node/left/image_rect_color", Image, image_callback)

# Initialize an OpenCV Window named "Image Window"
# cv2.namedWindow("Image Window", 1)

# Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
while not rospy.is_shutdown():
    rospy.spin()