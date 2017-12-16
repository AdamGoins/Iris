import cv2
import numpy as np

from src.base.overlay.border.Border import Border
from src.base.overlay.line.Line import Line


class Overlay:

    def __init__(self, image):
        self.image = image
        self.createOverlay()

    def createOverlay(self):

        self.mask = np.zeros(self.image.rows. self.image.cols)
        self.createBorder()


    def createBorder(self):


        lineSize = 100
        vertices = Border.getBoundingBox()

        for i in range(4):

            cornerPiece1 = Line(lineSize, 0,)

    