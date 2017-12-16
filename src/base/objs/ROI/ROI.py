

"""
ROI - Region of Interest
"""
from src.base.objs.Rectangle.Rectangle import Rectangle


class ROI(Rectangle):


    def __init__(self, image, superframe, ROI):
        super().__init__(ROI.x, ROI.y, ROI.relativeWidth, ROI.relativeHeight)
        self.result     = image
        self.superframe = superframe
        self.ROI = ROI

    def innerROI(self, rect):
        rect.setX(self.x + rect.x)
        rect.setY(self.y + rect.y)
        return rect

    def drawROI(self, thickness=1):
        self.superframe.drawRect(self.ROI, thickness)

    def superframe(self):
        return self.superframe

