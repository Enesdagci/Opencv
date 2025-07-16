import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode


frameWidth = 720 
frameHeight = 480

cap = cv.VideoCapture(0)

while True:
    status, frame = cap.read()
    frame = cv.resize(frame, (frameWidth, frameHeight))

    for qr in decode(frame):
        mydata = qr.data.decode("utf-8")

        points_1 = np.array([qr.polygon],np.int32)
        points_1 = np.reshape(points_1,(-1,1,2))
        points_2 = qr.rect

        print(mydata)
        cv.polylines(frame,[points_1],True,(0,0,255),3)
        cv.putText(frame,mydata,(points_2[0],points_2[2]),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv.imshow("Video Capture", frame)
    
    if cv.waitKey(1) == ord("q"):
        break


cv.destroyAllWindows()
