import numpy as np
import cv2 as cv


def rescaling_frame(frame, scale= 1.5):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimension = (height, width)

    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)


cap = cv.VideoCapture(0)

ret, frame = cap.read()
if not ret:
    print("Cannot read frame ...")
    cap.release()
    exit()

height, width = frame.shape[:2]

fourcc = cv.VideoWriter_fourcc(*"XVID")
out = cv.VideoWriter("output.avi", fourcc, 20.0, (width, height))

while True:
    if not ret:
        print("Can not receive frame. Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_resize = rescaling_frame(frame)


    out.write(frame)          # Renkli kareyi kaydet
    cv.imshow('frame', gray)  # Gri tonlamalı göster
    cv.imshow('resized_frame', frame_resize)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()

