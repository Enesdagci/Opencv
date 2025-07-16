import cv2 as cv
import numpy as np

img = cv.imread('pictures/master_card.webp')

width, height = 240, 360
points_1 = np.float32([[440, 370],[1005,150],[610,260],[1070,500]])
points_2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv.getPerspectiveTransform(points_1,points_2)
output = cv.warpPerspective(img,matrix,(width,height))

for x in range(0,4):
    cv.circle(img, (int(points_1[x][0]),int(points_1[x][1])),5,(0,255,0))

cv.imshow("Deneme",img)
cv.imshow("Detected",output)

cv.waitKey(0)
cv.destroyAllWindows()
