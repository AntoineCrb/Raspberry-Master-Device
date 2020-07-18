import cv2
import numpy as np
 
# get lines
def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    kernel = 15 # it's important here to have a high value to prevent the light reflection of the road to cause any problem
    blur = cv2.GaussianBlur(gray,(kernel, kernel),0)
    canny = cv2.Canny(blur, 50, 150)
    return canny