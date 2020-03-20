# example for image_name (lane_image.png -> image_name = lane_image )
# call the function traffic_signal to get the output

import cv2 as cv
import numpy as np

def traffic_signals(image_name):

  # read the image
  image = cv.imread(str(image_name)+'.png')

  #convert the image from BGR to HSV format
  image_hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)

  # define lower and upper range values for the colors in traffic signals
  if image[228,round(image.shape[1]/2)][2] == 255:
    lower_range = np.array([0,100,100])
    upper_range = np.array([5,255,255])
  elif image[704,round(image.shape[1]/2)][1] == 255:
    lower_range = np.array([55,100,100])
    upper_range = np.array([65,255,255])
  elif image[456,round(image.shape[1]/2)][1] == 255:
    lower_range = np.array([20,190,20])
    upper_range = np.array([30,255,255])                  

  # mask the region of the traffic signal
  mask_image    = cv.inRange(image_hsv, lower_range, upper_range)

  # print the signal color according to pixel values at the centre of each masked signals
  if mask_image[228,round(mask_image.shape[1]/2)] == 255:
    print("The signal color is RED")
  elif mask_image[456,round(mask_image.shape[1]/2)] == 255:
    print("The signal color is YELLOW")
  elif mask_image[704,round(mask_image.shape[1]/2)]== 255:
     print("The signal color is GREEN")

  return
