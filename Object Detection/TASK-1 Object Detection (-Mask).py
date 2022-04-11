# GRIP : THE SPARKS FOUNDATION
# IoT & Computer Vision

# Shreyas Puranik
# TASK-1 

import cv2 as cv
import numpy as np

ref = cv.imread('C:/Users/USER/Desktop/desktop/internship/2883180.jpg')

ref=cv.resize(ref,(int(356*2),int(256*2)))

# gaus = cv.GaussianBlur(ref,(5,5),2)

hsvr = cv.cvtColor(ref, cv.COLOR_BGR2HSV)

lower = np.array([140,50,50])

upper = np.array([255,255,255])

maskr = cv.inRange(hsvr, lower, upper)

maskr0 = cv.dilate(maskr, None, iterations=3)

maskr1 = cv.erode(maskr, None, iterations=2)

cv.imshow("Image",ref)

# cv.imshow("Gaus",gaus)

cv.imshow("Mask",maskr)

cv.waitKey(20)
