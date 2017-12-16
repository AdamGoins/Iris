import cv2
import numpy as np

class Overlay:

    def __init__(self, image):
        self.image = image
        self.createOverlay()

    def createOverlay(self):

        self.mask = np.zeros(self.image.rows. self.image.cols)
        lineSize = 50

        for i in range(4):


    