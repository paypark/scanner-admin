class CaptureSettings(object):

    def __init__(self):
        self.shutterSpeed = 0
        self.frameRate = 30

    def getShutterSpeed(self):
        return self.shutterSpeed

    def setShutterSpeed(self, shutterSpeed):
        self.shutterSpeed = shutterSpeed
        return self

    def getFrameRate(self):
        return self.frameRate

    def setFrameRate(self, frameRate):
        self.frameRate = frameRate
        return self

    def set(self, newSettings):
        self.frameRate = newSettings['frameRate']
        self.shutterSpeed = newSettings['shutterSpeed']

    def toJSON(self):
        return dict(
            frameRate=self.frameRate,
            shutterSpeed=self.shutterSpeed
        )
