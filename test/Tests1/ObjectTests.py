
import os

import cv2

cap = cv2.VideoCapture(0)
templates_dir = "../../assets/templates/"
template_array = list(os.listdir(templates_dir))

templates = []

for file in template_array:
    template = cv2.imread(templates_dir + file, 0)
    templates.append(template)

orb = cv2.ORB_create()


kps  = []
dess = []
for template in templates:
    kp2, des2 = orb.detectAndCompute(template, None)
    kps.append(kp2)
    dess.append(des2)


while True:

    _, frame = cap.read()
    #frame = cv2.imread("keyboard3.png")
    gray = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (1, 1), 0)
    edged = cv2.Canny(blurred, 50, 150)

    ret, thresh = cv2.threshold(edged, 127, 255, 50)


    # find contours in the edge map
    (_, cnts, __) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]


    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)

    largest_areas = sorted(cnts, key=cv2.contourArea, reverse=True)[:3]

    cv2.imshow("x", edged)
    cv2.imshow("original", frame)


    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()