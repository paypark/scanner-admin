import io
import time
import uuid
import picamera
from base_camera import BaseCamera

class Camera(BaseCamera):

    def __init__(self, cameraSettings):
        Camera.cameraInstance = picamera.PiCamera()
        super(Camera, self).__init__()
        time.sleep(2)
        Camera.cameraInstance.shutter_speed = cameraSettings.getShutterSpeed()
        Camera.isRecording = False

    @staticmethod
    def updateSettings(cameraSettings):
        Camera.pause()
        Camera.cameraInstance.shutter_speed = cameraSettings.getShutterSpeed()
        Camera.resume()

    @staticmethod
    def frames():
        Camera.isRecording = True
        stream = io.BytesIO()
        for _ in Camera.cameraInstance.capture_continuous(
                stream, 'jpeg', use_video_port=True):

            if not Camera.isRecording:
                break;

            # return current frame
            stream.seek(0)
            yield stream.read()

            # reset stream for next frame
            stream.seek(0)
            stream.truncate()

    @staticmethod
    def snapshot():
        time.sleep(2)
        filename = str(uuid.uuid4()) + ".jpg"
        Camera.cameraInstance.capture(filename)
        return filename

    @staticmethod
    def pause():
        print("pause()")
        Camera.isRecording = False

    @staticmethod
    def resume():
        print("resume()")
        Camera.isRecording = True
