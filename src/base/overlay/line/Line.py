import math

import cv2

from src.base.overlay.point.Point import Point
import numpy as np

class Line:

    SOLID  = 0
    DASHED = 1

    def __init__(self, point, angle=0, length=10, lineType=SOLID):

        self.origin = point

        self.lineType = lineType
        self.angle    = angle
        self.length   = length

        self.updateEndpoint()

    #     cv2.namedWindow("Line")
    #     cv2.createTrackbar('P1 X', 'Line', 0, 500, self.update)
    #     cv2.createTrackbar('P1 Y', 'Line', 0, 500, self.update)
    #
    #     cv2.createTrackbar('Length', 'Line', 0, 500, self.update)
    #     cv2.createTrackbar('Angle', 'Line', 0, 360, self.update)
    #
    # def update(self, x):
    #     self.origin.x = cv2.getTrackbarPos('P1 X', 'Line')
    #
    #     self.origin.y = cv2.getTrackbarPos('P1 Y', 'Line')
    #
    #     self.setLength(cv2.getTrackbarPos("Length", "Line"))
    #     self.setAngle(cv2.getTrackbarPos("Angle", "Line"))


    def x(self):
        return self.origin.x

    def y(self):
        return self.origin.y

    def translateX(self, translation):
        self.origin.translateX(translation)
        self.origin.translateX(translation)

    def translateY(self, translation):
        self.origin.translateY(translation)
        self.origin.translateY(translation)

    def getLength(self):
        return self.length

    def setLength(self, length):
        self.length = length
        self.updateEndpoint()


    def angle(self):
        return self.angle


    def setAngle(self, angle):
        self.angle = angle
        self.updateEndpoint()


    def updateEndpoint(self):
        x2 = int(self.origin.x + self.length * math.cos(math.radians(self.angle)))
        y2 = int(self.origin.y + self.length * math.sin(math.radians(self.angle)))
        self.endPoint = Point(x2, y2)

    def draw(self, image, color=(255, 0, 0), thickness=2):
        cv2.line(image, self.origin.origin(), self.endPoint.origin(), color, thickness, 8, 0)

    def copy(self):
        return Line(self.origin, self.length, self.angle)


# img = np.zeros((1000,1000,3), np.uint8)
# line = Line(Point(50, 50))
#
# while(1):
#     img = np.zeros((1000, 1000, 3), np.uint8)
#
#     line.draw(img)
#     cv2.imshow('image', img)
#     k = cv2.waitKey(1) & 0xFF
#
#
#     if k == 27:
#         break
#
#
# cv2.destroyAllWindows()