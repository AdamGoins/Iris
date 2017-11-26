from src.base.objs.CascadeObject.CascadeObject import CascadeObject
from src.base.objs.Frame.Frame import Frame
from src.base.objs.Rectangle.Rectangle import Rectangle
import cv2

class Face(Frame):

    eyeCascade = CascadeObject(CascadeObject.EYE)
    mouthCascade = CascadeObject(CascadeObject.MOUTH)
    noseCascade = CascadeObject(CascadeObject.NOSE)

    def __init__(self, image):
        super().__init__(image)

        self.result = image

        self.readFacialFeatures()

    def readFacialFeatures(self):
        self.eyes  = self.detectEyes()
        self.mouth = self.detectMouth()
        self.nose  = self.detectNose()

    def showEyes(self):
        eyeCount = 0
        for x, y, w, h in self.eyes:
            eyeCount += 1
            ROI = Rectangle(x, y, w, h)
            eyeFrame = self.grabROI(ROI)
            cv2.imshow("Eye: [" + str(eyeCount) + "]", eyeFrame)



    def detectEyes(self):
        self.eyes = Face.eyeCascade.detect(self.result)
        return self.eyes

    def detectMouth(self):
        self.mouth = Face.mouthCascade.detect(self.result)
        return self.mouth

    def detectNose(self):
        self.nose = Face.mouthCascade.detect(self.result)
        return self.nose

    def setEyeCascade(self, eyeCascade):
        Face.eyeCascade = eyeCascade

    def setMouthCascade(self, mouthCascade):
        Face.mouthCascade = mouthCascade

    def setNoseCascade(self, noseCascade):
        Face.noseCascade = noseCascade

