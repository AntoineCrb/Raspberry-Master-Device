from picamera import PiCamera
from picamera.array import PiRGBArray

class Camera:
    camera={}
    raw_capture={}

    def __init__(self, fps=30):
        self.camera = PiCamera()
        self.camera.rotation = 180
        self.camera.resolution = (1280, 720)
        self.camera.framerate = fps
        self.raw_capture = PiRGBArray(self.camera)

    def capture(self):
        self.camera.capture(self.raw_capture, format="bgr")
        return self.raw_capture.array

    def get_camera(self): return self.camera
    def get_raw_camera(self): return self.raw_capture

    def clear(self): self.raw_capture.truncate(0)
