import cv2
import imutils

from lib.IrisImageUtils.Shapes.ShapeDetection import *
from src.base.objs.CascadeObject.CascadeObject import CascadeObject
from src.base.objs.DepthPerception import DepthPerception
from src.base.objs.Face.Face import Face
from src.base.objs.Frame.Frame import Frame
from src.base.objs.Rectangle.Rectangle import Rectangle
from src.base.objs.modules.Threshold.Threshold import Threshold
from src.base.objs.modules.GaussianBlur.GaussianBlur import GaussianBlur


def main():

    cap = cv2.VideoCapture(1)
    threshold = Threshold()
    blur = GaussianBlur()
    faceDetector = CascadeObject(CascadeObject.FACE_FRONTAL_ALT)
    images = []

    depthPerceptor = DepthPerception.DepthPerception()

    faceDetector = CascadeObject(CascadeObject.FACE_FRONTAL_ALT)
    while True:

        _, frame = cap.read()

        images = images[0:10]
        # convert the image to grayscale, blur it, and find edges
        # in the image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        blurred = blur.blur(gray)


        bigImage = Frame(frame)
        # s1 = Frame(threshold.adaptiveThreshold2(blurred,127, Threshold.ADAPTIVE_GAUSSIAN, Threshold.BINARY_INV, 3, 0))
        # s1.show()
        #
        # images.insert(0, gray)
        # disparity = depthPerceptor.getDisparityMap(images)
        #
        # dis = Frame(disparity)


        faceDetector.detect(frame)
        for faceROI in faceDetector.resultsAsROI():
            subFrame = Frame(bigImage.grabROI(faceROI))
            subFrame.putText("Face", faceROI)
            subFrame.show()

        # (_, cnts, __) = cv2.findContours(s1.result.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
        # # loop over our contours
        #
        #
        # for c in cnts:
        #
        #     x, y, w, h = cv2.boundingRect(c)
        #     shape = get_shape(c)
        #     if shape == "Rectangle":
        #         cv2.imshow("Rect", frame[y: y+h + 50, x:x+w + 50])
        #     cv2.putText(frame, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 125) )
        #
        # cv2.drawContours(frame, cnts, -1, (0, 255, 0), 1)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cv2.destroyAllWindows()
    cap.release()


main()