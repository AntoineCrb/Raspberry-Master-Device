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
    try:
        loop()
    except:
        print('error')
        control.stop()

def loop():
    while True:
        frame = vs.read()
        canny = algo.canny(frame)

        cropped_canny = algo.region_of_interest(canny)
        lines = cv2.HoughLinesP(cropped_canny, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)

        averaged_lines = algo.average_slope_intercept(cropped_canny, lines)

        line_image = algo.display_lines(cropped_canny, averaged_lines)
        combo_image = cv2.addWeighted(cropped_canny, 0.8, line_image, 1, 1)

        x = algo.get_average_slopes(averaged_lines)

        if x is None: control.stop()
        elif -0.15 < x < -0.08: control.left2()
        elif x < -0.05: control.left1()
        elif x < 0.05: control.forward()
        elif x < 0.08: control.right1()
        elif x < 0.15: control.right2()
        else: control.stop()
        
        if x is not None: print(x)

        cv2.imshow("Result", combo_image)
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"): 
            control.stop()
            break
        fps.update()
    
    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    cv2.destroyAllWindows()
    vs.stop()

init()