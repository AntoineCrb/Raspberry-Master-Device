import cv2
import numpy as np
from camera.camera import Camera
from communication.control import Control
import algo
import threading

fps = 10

camera = Camera()
control = Control()


def loop():
    image = cv2.imread(camera.capture)
    lane_image = np.copy(image)
    camera.clear()

    canny = algo.canny(lane_image)
    cv2.imshow(canny)
    threading.Timer(1/fps, loop).start()

loop()