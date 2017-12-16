from src.base.objs.Rectangle.Rectangle import Rectangle
import cv2

from src.base.overlay.line.Line import Line
import numpy as np

from src.base.overlay.point.Point import Point


class Border(Rectangle):

    LINE   = 0
    DOTTED = 1
    DASHED = 2
    FRAMED = 3

    def __init__(self, rect, borderType=LINE, thickness=1, color=(200,200,200)):
        super().__init__(rect.x, rect.y, rect.width, rect.height)
        self.borderType = borderType
        self.thickness  = thickness
        self.color      = color
        self.lines      = []

        self.createBorder()

    def createBorder(self):

        img = np.zeros((1000, 1000, 3), np.uint8)

        vertices = self.getBoundingBox()
        width  = self.width
        height = self.height

        for i in range(len(vertices)):
            rotation = i * 90
            length = width if i % 2 == 0 else height
            line = Line(vertices[i], angle=rotation,length=length, lineType=self.borderType)
            print(line.origin.origin(), ":", line.length)
            line.draw(img)



    def createDashedBorder(self):

        img = np.zeros((1000, 1000, 3), np.uint8)
        vertices = self.getBoundingBox()

        width  = self.width
        height = self.height
        lines  = []
        for i in range(len(vertices)):
            rotation = 90 * i
            length = width if i % 2 == 0 else height
            line = Line(vertices[i], angle=rotation,length=length)
            cv2.putText(img, str(rotation), line.origin.origin(), 1, 5, self.color, self.thickness)
            lines.append(line)

        for line in lines:
            line.draw(img)
            cv2.line(img, line.origin.origin(), line.endPoint.origin(), (255,255, 0), 1, 8, 0)
        cv2.imshow("Oh", img)

    def getBoundingBox(self):
        vertex1 = Point(self.x, self.y)
        vertex2 = Point(self.relativeWidth, self.y)
        vertex3 = Point(self.relativeWidth, self.relativeHeight)
        vertex4 = Point(self.x, self.relativeHeight)

        vertices = (vertex1, vertex2, vertex3, vertex4)
        return vertices



    def draw(self, image):
        for line in self.lines:
            line.draw(image)


img = np.zeros((1000,1000,3), np.uint8)
rect = Rectangle(50, 50, 125, 90)
border = Border(rect, Border.LINE, 2)

while(1):
    img = np.zeros((1000, 1000, 3), np.uint8)

    border.draw(img)
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF


    if k == 27:
        break


cv2.destroyAllWindows()