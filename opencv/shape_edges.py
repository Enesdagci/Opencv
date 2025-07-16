import cv2 as cv
import numpy as np 

capture = cv.VideoCapture(0)

capture.set(cv.CAP_PROP_FRAME_WIDTH, 720)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    _, frame = capture.read()

    cv.imshow("Video Capture", frame)

    if cv.waitKey(1) == ord("q"):
        break

cv.destroyAllWindows()
