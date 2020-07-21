import cv2
import numpy as np
from imutils.video import VideoStream, FPS
import time

from communication.control import Control
import algo

control = Control()
vs = VideoStream(usePiCamera=True, resolution=(640, 480), framerate=32, rotation=180)
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

        cropped_canny = algo.region_of_interest(canny)
        lines = cv2.HoughLinesP(cropped_canny, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
        cv2.imshow("result", frame)    
        cv2.imshow("Canny", canny)



        key = cv2.waitKey(1) & 0xFF
        if key == ord('z'): control.forward()
        elif key == ord('s'): control.backward()
        elif key == ord('d'): control.right_spin()
        elif key == ord('q'): control.left_spin()
        elif key == ord('e'): break
        else: control.stop()
        fps.update()
    
    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    cv2.destroyAllWindows()
    vs.stop()

init()