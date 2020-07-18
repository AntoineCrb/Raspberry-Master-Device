import cv2
import numpy as np
from camera.camera import Camera
from communication.control import Control
import algo

camera = Camera()
control = Control()

while 1: # loop
    image = cv2.imread(camera.capture)
    lane_image = np.copy(image)
    camera.clear()

    algo.canny(lane_image)