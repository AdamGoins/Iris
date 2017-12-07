import math

import cv2

from src.base.overlay.point.Point import Point
import numpy as np

class Line:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        #
        # cv2.namedWindow("Line")
        # cv2.createTrackbar('P1 X', 'Line', 0, 500, self.update)
        # cv2.createTrackbar('P1 Y', 'Line', 0, 500, self.update)
        #
        # cv2.createTrackbar('P2 X', 'Line', 0, 500, self.update)
        # cv2.createTrackbar('P2 Y', 'Line', 0, 500, self.update)
        #
        # cv2.createTrackbar('Length', 'Line', 0, 500, self.update)
        # cv2.createTrackbar('Angle', 'Line', 0, 360, self.update)

    # def update(self, x):
    #     self.point1.x = cv2.getTrackbarPos('P1 X', 'Line')
    #
    #     self.point1.y = cv2.getTrackbarPos('P1 Y', 'Line')
    #     self.point2.x = cv2.getTrackbarPos('P2 X', 'Line')
    #     self.point2.y = cv2.getTrackbarPos('P2 Y', 'Line')
    #
    #     self.setLength(cv2.getTrackbarPos("Length", "Line"))
    #     self.setAngle(cv2.getTrackbarPos("Angle", "Line"))




    def translateX(self, translation):
        self.point1.translateX(translation)
        self.point2.translateX(translation)

    def translateY(self, translation):
        self.point1.translateY(translation)
        self.point2.translateY(translation)

    def length(self):
        # Distance between two points: sqrt( (x2 - x1)^2 - (y2 - y1)^2 )
        distance = int( math.fabs( ( ( self.point2.x - self.point1.x ) ** 2 - ( self.point2.y - self.point1.y ) ** 2 ) ) ** (0.5) )
        return distance

    def setLength(self, length):
        angle = self.angle()
        self.updateLine(length, angle)

    def angle(self):
        angle = float(math.atan((self.point1.y - self.point2.y) / (self.point2.x - self.point1.x)) * 180 / math.pi)
        return angle

    def setAngle(self, angle):
        length = self.length()
        self.updateLine(length, angle)

    def updateLine(self, length, angle):
        x2 = int(self.point1.x + length * math.cos(math.radians(angle)))
        y2 = int(self.point1.y + length * math.sin(math.radians(angle)))
        self.point2 = Point(x2, y2)

    def draw(self, image, color=(255, 0, 0), thickness=2):
        cv2.line(image, self.point1.origin(), self.point2.origin(), color, thickness, 8, 0)


# img = np.zeros((1000,1000,3), np.uint8)
# line = Line(Point(50, 50), Point(125, 125))
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