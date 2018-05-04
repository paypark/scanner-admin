import time
import uuid
import os
from base_camera import BaseCamera

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    imgs = [open(os.path.join(__location__, f + '.jpg'), 'rb').read() for f in ['1', '2', '3']]

    def __init__(self, cameraSettings):
        super(Camera, self).__init__()
        Camera.shutter_speed = cameraSettings.getShutterSpeed()
        Camera.isRecording = False

    @staticmethod
    def updateSettings(cameraSettings):
        Camera.shutter_speed = cameraSettings.getShutterSpeed()
        print("updateSettings()")

    @staticmethod
    def frames():
        while True:
            time.sleep(1)
            yield Camera.imgs[int(time.time()) % 3]

    @staticmethod
    def snapshot():
        return str(uuid.uuid4()) + ".jpg"
