import cv2
import numpy as np
from imutils.video import VideoStream, FPS
import time

from communication.control import Control
import algo

control = Control()
vs = VideoStream(usePiCamera=True, resolution=(1280, 720), framerate=32, rotation=180)
fps = FPS()

def init():
    vs.start()
    time.sleep(2.0)
    fps.start()
    loop()

def loop():
    while True:
        frame = vs.read()
        canny = algo.canny(frame)

        cv2.imshow("Frame", frame)
        cv2.imshow("Canny", canny)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('z'): control.forward()
        elif key == ord('s'): control.backward()
        elif key == ord('d'): control.right_spin()
        elif key == ord('q'): control.left_spin()
        elif key == ord("q"): break
        else: control.stop()
        fps.update()
    
    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    cv2.destroyAllWindows()
    vs.stop()

init()