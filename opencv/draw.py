import cv2 as cv
import numpy as np

width, height = 720, 480
center_x, center_y = 360, 240

img = cv.imread("pictures/white_screen.png")
img_resized = cv.resize(img,(width, height))

cv.line(img_resized,(center_x, center_y-10),(center_x, center_y+10),(0,0,0),2)

cv.line(img_resized,(center_x-10,center_y),(center_x+10,center_y),(0,0,0),2)

cv.imshow("Resized", img_resized)

cv.waitKey(0)
cv.destroyAllWindows()

