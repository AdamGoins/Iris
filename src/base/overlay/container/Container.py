import cv2

from src.base.objs.Rectangle.Rectangle import Rectangle


class Container(Rectangle):

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def addChild(self, child):

        cv2.ellipse()
