import cv2 as cv
import sys

img = cv.imread("pictures/nebula.jpg")

if img is None:
  sys.exit("resim okunmadı")

cv.imshow("Stars", img)

cv.waitKey(0)

