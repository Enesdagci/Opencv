import cv2
import numpy as np

image = cv2.imread(".\\images\\shapes.png")
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
size = cv2.magnitude(sobel_x, sobel_y)

grey_sobel_x = cv2.Sobel(grey_image, cv2.CV_64F, 1, 0, ksize=3)
grey_sobel_y = cv2.Sobel(grey_image, cv2.CV_64F, 0, 1, ksize=3)
grey_size = cv2.magnitude(grey_sobel_x, grey_sobel_y)

canny_image = cv2.Canny(image, 50, 150)
canny_image1 = cv2.Canny(image, 100, 200)
canny_image2 = cv2.Canny(image, 200, 250)

blurred_image = cv2.blur(image, (5,5))
blurred_canny_image = cv2.Canny(blurred_image, 50, 150)

sx = cv2.Sobel(grey_image, cv2.CV_64F, 1, 0, ksize=3)
print(sx.min(), sx.max())

y = grey_image.shape[0] // 2
yr = np.nonzero(sx[y])[0]
print(yr)
print(sx[y, yr])
print(cv2.convertScaleAbs(sx).dtype, cv2.convertScaleAbs(sx).max())

### Images Shows
cv2.imshow("Orijinal Gorsel", image)

# Sobel Original Image
cv2.imshow("Sobl x", cv2.convertScaleAbs(sobel_x))
cv2.imshow("Soble y", cv2.convertScaleAbs(sobel_y))
cv2.imshow("Size", cv2.convertScaleAbs(size))

# Sobel Grey image
cv2.imshow("Grey Sobel x", cv2.convertScaleAbs(grey_sobel_x))
cv2.imshow("Grey Sobel y", cv2.convertScaleAbs(grey_sobel_y))
cv2.imshow("Grey Image Size", cv2.convertScaleAbs(grey_size))

cv2.imshow("Alpha", cv2.convertScaleAbs(sx))
cv2.imshow("Alpha 0.25", cv2.convertScaleAbs(sx,alpha=0.25))

cv2.imshow("Canny Image", canny_image)
cv2.imshow("Canny Image1", canny_image1)
cv2.imshow("Canny Image2", canny_image2)

cv2.imshow("Blurred Canny", blurred_canny_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

