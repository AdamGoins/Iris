from src.base.objs.Rectangle.Rectangle import Rectangle
import cv2

from src.base.overlay.line.Line import Line
from test.Tests1.Rectangle import Point
import numpy as np

class Border(Rectangle):

    LINE   = 0
    DOTTED = 1
    DASHED = 2
    FRAMED = 3

    def __init__(self, x, y, w, h, borderType=LINE, thickness=1, color=(200,200,200)):
        super().__init__(x, y, w, h)
        self.borderType = borderType
        self.thickness  = thickness
        self.color      = color
        self.lines      = []

    def createLinedBorder(self):

        vertex1 = Point(self.x, self.y)
        vertex2 = Point(self.x, self.relativeHeight)
        vertex3 = Point(self.relativeWidth, self.y)
        vertex4 = Point(self.relativeWidth, self.relativeHeight)

        line1 = Line(vertex1, vertex2)
        line2 = Line(vertex1, vertex3)
        line3 = Line(vertex2, vertex4)
        line4 = Line(vertex3, vertex4)

        self.lines.append(line1)
        self.lines.append(line2)
        self.lines.append(line3)
        self.lines.append(line4)

    def draw(self, image):
        for line in self.lines:
            line.draw(image)


img = np.zeros((1000,1000,3), np.uint8)
border = Border(img)

while(1):
    img = np.zeros((1000, 1000, 3), np.uint8)

    border.draw(img)
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF


    if k == 27:
        break


cv2.destroyAllWindows()