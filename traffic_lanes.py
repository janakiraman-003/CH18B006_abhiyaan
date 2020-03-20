# name your image as line_image.jpeg to get the output
# this code is specific to the image given and cannot be generalised

import cv2
import numpy as np

# read the image
img = cv2.imread('line_image.jpeg')

# conver the image into grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# detect the edges using canny detection
edges = cv2.Canny(gray,50,150,apertureSize = 3)

#  detect the parameters for lines (rho, theta) using hough transform algorithm
lines = cv2.HoughLines(edges,2,np.pi/100,230)

# convert rho, theta into x and y coordinates
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 200*(-b))
    y1 = int(y0 + 200*(a))
    x2 = int(x0 - 200*(-b))
    y2 = int(y0 - 200*(a))

# draw lines from the found values of (x_start,y_start),(x_end,y_end)
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

# convert rho, theta into x and y coordinates
for rho,theta in lines[1]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 180*(-b))
    y1 = int(y0 + 180*(a))
    x2 = int(x0 - 180*(-b))
    y2 = int(y0 - 180*(a))

# draw lines from the found values of (x_start,y_start),(x_end,y_end)
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

# convert rho, theta into x and y coordinates
for rho,theta in lines[2]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 300*(-b))
    y1 = int(y0 + 300*(a))
    x2 = int(x0 - 300*(-b))
    y2 = int(y0 - 300*(a))

# draw lines from the found values of (x_start,y_start),(x_end,y_end)
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

# convert rho, theta into x and y coordinates
for rho,theta in lines[10]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 - 1000*(-b))
    y1 = int(y0 - 1000*(a))
    x2 = int(x0 - 600*(-b))
    y2 = int(y0 - 600*(a))

# draw lines from the found values of (x_start,y_start),(x_end,y_end)
    cv2.line(img,(x2,y2),(x1,y1),(0,0,255),2)

# convert rho, theta into x and y coordinates
for rho,theta in lines[11]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 - 1000*(-b))
    y1 = int(y0 - 1000*(a))
    x2 = int(x0 - 800*(-b))
    y2 = int(y0 - 800*(a))

# draw lines from the found values of (x_start,y_start),(x_end,y_end)
    cv2.line(img,(x2,y2),(x1,y1),(0,0,255),2)

# convert rho, theta into x and y coordinates
for rho,theta in lines[13]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 - 1000*(-b))
    y1 = int(y0 - 1000*(a))
    x2 = int(x0 - 600*(-b))
    y2 = int(y0 - 600*(a))

# draw lines from the found values of (x_start,y_start),(x_end,y_end)
    cv2.line(img,(x2,y2),(x1,y1),(0,0,255),2)

# convert rho, theta into x and y coordinates
for rho,theta in lines[21]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 - 1000*(-b))
    y1 = int(y0 - 1000*(a))
    x2 = int(x0 - 600*(-b))
    y2 = int(y0 - 600*(a))

# draw lines from the found values of (x_start,y_start),(x_end,y_end)
    cv2.line(img,(x2,y2),(x1,y1),(0,0,255),2)

# convert rho, theta into x and y coordinates
for rho,theta in lines[31]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 - 1000*(-b))
    y1 = int(y0 - 1000*(a))
    x2 = int(x0 - 600*(-b))
    y2 = int(y0 - 600*(a))

# draw lines from the found values of (x_start,y_start),(x_end,y_end)
    cv2.line(img,(x2,y2),(x1,y1),(0,0,255),2)
           
# save the final image
cv2.imwrite('lane_highlited_image.jpg',img)
