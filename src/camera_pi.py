import io
import time
import uuid
import picamera
from base_camera import BaseCamera


class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            # let camera warm up
            time.sleep(2)

            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
    
    @staticmethod
    def snapshot():
        with picamera.PiCamera() as camera:
            time.sleep(2)
            filename = str(uuid.uuid4()) + ".jpg"
            camera.capture(filename)
            return filename


