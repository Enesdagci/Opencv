import cv2
import numpy as np

image = cv2.imread(".\\images\\Icon-192.png")

a = np.full((2,2), 100, dtype=np.uint8)
b = np.full((2,2), 200, dtype=np.uint8)

#### İmage procces
# Canal split
b, g, r = cv2.split(image)

# Bgr to rgb
fixed_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Grey convert
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grey_image1 = image[::,0].astype(np.uint8)

# Split
image_copy = image.copy()

# Image masking
image_copy[0:50,0:50] = [0,255,0]

# Threshold
_, image_thres = cv2.threshold(grey_image, 50, 255, cv2.THRESH_BINARY)
_, image_thres1 = cv2.threshold(grey_image, 127, 255, cv2.THRESH_BINARY)
_, image_thres2 = cv2.threshold(grey_image, 200, 255, cv2.THRESH_BINARY)

# Added images
added_image = cv2.add(image, np.array([80], dtype=np.uint8))
subtract_image = cv2.subtract(image, np.array([80], dtype=np.uint8))

 
#### Terminal outputs
# Temel Görsel
print(image.shape)
print(image.dtype)
print(image[100,200],"\n")

# BGR TO RGB
print(fixed_image.shape)
print(fixed_image.dtype)
print(fixed_image[100,200],"\n")

# GREY COLOR 
print(grey_image.shape)
print(grey_image.dtype)
print(grey_image[100,200], "\n")


# Image shows
cv2.imshow("Medal of Honor", image)
cv2.imshow("RGB Medal Of Honor", fixed_image)
cv2.imshow("Grey Medal of Honor", grey_image)

cv2.imshow("Grey Medal of Honor", grey_image1)

cv2.imshow("Blue canal", b)
cv2.imshow("Green canal", g)
cv2.imshow("Red canal", r)

cv2.imshow("Painted Image", image_copy)

cv2.imshow("Threshold Image(50)", image_thres)
cv2.imshow("Threshold Image(127)", image_thres1)
cv2.imshow("Threshold Image(200)", image_thres2)

cv2.imshow("Lighted Image", added_image)
cv2.imshow("Darkened Image", subtract_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
