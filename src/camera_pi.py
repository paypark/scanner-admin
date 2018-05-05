import io
import time
import uuid
import picamera
from base_camera import BaseCamera
import datetime

class Camera(BaseCamera):

    cameraInstance = picamera.PiCamera()
    isRecording = False

    def __init__(self, cameraSettings):
        super(Camera, self).__init__()
        time.sleep(10)
        Camera.updateSettings(cameraSettings)

    @staticmethod
    def updateSettings(cameraSettings):
        Camera.cameraInstance.framerate = cameraSettings.getFrameRate()
        Camera.cameraInstance.shutter_speed = cameraSettings.getShutterSpeed()
        Camera.cameraInstance.iso = cameraSettings.getIso()
        Camera.cameraInstance.resolution = (cameraSettings.getWidth(), cameraSettings.getHeight())

    @staticmethod
    def frames():
        stream = io.BytesIO()
        for _ in Camera.cameraInstance.capture_continuous(
                stream, 'jpeg', use_video_port=True):

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
    def startRecording():
        if Camera.isRecording == False:
            Camera.isRecording = True
            timestamp = time.time()
            dateTimeString = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d-%H:%M:%S')
            fileName = dateTimeString + ".h264"
            Camera.cameraInstance.start_recording(fileName)

    @staticmethod
    def stopRecording():
        if Camera.isRecording == True:
            Camera.isRecording = False
            Camera.cameraInstance.stop_recording()

    @staticmethod
    def isCameraRecording():
        return Camera.isRecording
