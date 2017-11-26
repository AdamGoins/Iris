import cv2

from src.base.objs.Color.Color import Color
from src.base.objs.Showable.Showable import Showable
from src.base.objs.Rectangle.Rectangle import Rectangle
from src.base.objs.Transformation.Transformations import Transformable
from src.base.objs.Drawable.Drawable import Drawable

class Frame(Transformable, Drawable, Showable):

    LEFT  = 0
    RIGHT = 1
    ABOVE = 2
    BELOW = 3

    def __init__(self, image, name="Image Frame"):
        Transformable.__init__(self, image)
        Drawable.__init__(self)
        Showable.__init__(self)

        self.result = image
        self.name = name

    def grabROI(self, ROI):
        return self.crop(self.result, ROI)

    def drawRectangle(self, ROI, thickness=1):
        super().drawRect(self.result, ROI, thickness)

    def putText(self, text, ROI, type=ABOVE, font=Drawable.HERSHEY_TRIPLEX, scale=1, color=Color.GREEN, thickness=1,
                xOffset=0, yOffset=0):
        super().putText(self.result, text, ROI, type, font, scale, color, thickness, xOffset, yOffset)

