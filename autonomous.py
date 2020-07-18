import cv2
import numpy as np
from camera.camera import Camera
from communication.control import Control
import algo
import threading

fps = 0
camera = Camera()
control = Control()

def init(fps=10):
    fps = fps
    #camera = Camera()
    #control = Control()
    loop()

def loop():
    for frame in camera.get_camera().capture_continuous(camera.get_raw_camera(), format="bgr", use_video_port=True):
        image = np.copy(frame.array)
        canny = algo.canny(image)
        cv2.imshow(canny)
        camera.get_raw_camera().truncate(0)
        
        #threading.Timer(1/fps, loop).start()
    cv2.destroyAllWindows()



init()