class CaptureSettings(object):

    def __init__(self):
        self.shutterSpeed = 0
    
    def getShutterSpeed(self):
        return self.shutterSpeed
    
    def setShutterSpeed(self, shutterSpeed):
        self.shutterSpeed = shutterSpeed
        return self

    def set(self, newSettings):
        self.shutterSpeed = newSettings['shutterSpeed']

    def toJSON(self):
        return dict(
            shutterSpeed=self.shutterSpeed
        )
        