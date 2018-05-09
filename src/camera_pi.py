import io
import time
import uuid
import picamera
import threading
from base_camera import BaseCamera

from FilenameService import FilenameService
from USBStorageService import USBStorageService

class Camera(BaseCamera):

    cameraInstance = picamera.PiCamera()
    isRecording = False
    FILE_RECORDING_DURATION_IN_SECONDS = 60

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
            filePath = Camera.generateFilePath()
            print("startRecording() => " + filePath)
            Camera.cameraInstance.start_recording(filePath)
            threading.Thread(target=Camera.splitRecordingLoop).start()

    @staticmethod
    def stopRecording():
        if Camera.isRecording == True:
            print("stopRecording()")
            Camera.isRecording = False
            Camera.cameraInstance.stop_recording()

    @staticmethod
    def splitRecordingLoop():
        if Camera.isRecording == False:
            return
        filePath = Camera.generateFilePath()
        print("splitRecordingLoop() => " + filePath)
        Camera.cameraInstance.split_recording(filePath)
        Camera.cameraInstance.wait_recording(Camera.FILE_RECORDING_DURATION_IN_SECONDS)
        if Camera.isRecording == True:
            Camera.splitRecordingLoop()

    @staticmethod
    def isCameraRecording():
        return Camera.isRecording

    @staticmethod
    def generateFilePath():
        fileName = FilenameService.generateTimeBasedFilename('h264')
        return USBStorageService.getPath() + "/" + fileName

