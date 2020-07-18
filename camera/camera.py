from picamera import PiCamera
from picamera.array import PiRGBArray

class Camera:
    camera={}
    raw_capture={}

    def __init__(self):
        self.camera = PiCamera()
        self.camera.rotation = 180
        self.camera.resolution = (1280, 720)
        self.raw_capture = PiRGBArray(self.camera)

    def capture(self):
        self.camera.capture(self.raw_capture, format="bgr")
        return self.raw_capture.array

    def clear(self): self.raw_capture.truncate(0)
