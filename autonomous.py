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
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"): 
            break
        fps.update()
    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    cv2.destroyAllWindows()
    vs.stop()

    """for frame in camera.get_camera().capture_continuous(camera.get_raw_camera(), format="bgr", use_video_port=True):
        image = np.copy(frame.array)
        canny = algo.canny(image)
        cv2.imshow(canny)
        camera.get_raw_camera().truncate(0)
        
        #threading.Timer(1/fps, loop).start()
    cv2.destroyAllWindows()"""



init()