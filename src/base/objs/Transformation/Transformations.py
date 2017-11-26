import cv2


class Transformable():

    def __init__(self, image):
        self.result = image

    def resize(self, width=0, height=0):
        cv2.resize()

    def rotate(self, image, angle, scale=1.0):
        width  = image.cols
        height = image.rows
        midpoint       = (width / 2.0, height / 2.0)
        rotationMatrix = cv2.getRotationMatrix2D(midpoint, angle, scale)
        cv2.warpAffine(image, self.result, rotationMatrix,(width, height))
        return self.result

    def crop(self, image, rectangle):
        return image[rectangle.y:rectangle.relativeHeight, rectangle.x:rectangle.relativeWidth]


