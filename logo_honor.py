import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread(".\\images\\HappyFish.jpg")

#### İmage procces
# Canal split
b, g, r = cv2.split(image)

# Bgr to rgb
fixed_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Grey convert
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grey_image1= ((0.299 * r) + (0.587 * g )+ (0.114 *b)).astype(np.uint8)


# Split
image_copy = image.copy()

# Image masking
image_copy[0:50,0:50] = [0,255,0]

# Threshold
thres, image_thres = cv2.threshold(grey_image, 50, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thres1, image_thres1 = cv2.threshold(grey_image, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thres2, image_thres2 = cv2.threshold(grey_image, 200, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Added images
added_image = cv2.add(image, np.full(image.shape, 80, dtype=np.uint8))
subtract_image = cv2.subtract(image, np.full(image.shape, 80, dtype=np.uint8))

# Masking
masked_image = cv2.inRange(grey_image,30,60)
masked_image1 = cv2.inRange(grey_image,120,170)
masked_image2 = cv2.inRange(grey_image,200,250)

# Softing and Blurring
blurred_image = cv2.blur(image,(5,5))
blurred_image1 = cv2.blur(image,(10,10))
blurred_image2 = cv2.blur(image,(20,20))

grey_blurred_image = cv2.blur(image_thres,(10,10))
blurred_grey_image = cv2.cvtColor(blurred_image1, cv2.COLOR_BGR2GRAY)

 
#### Terminal outputs
# Simple image
print("Original image")
print(image.shape)
print(image.dtype)
print(image[100,200],"\n")

# BGR TO RGB
print("Bgr to rgb")
print(fixed_image.shape)
print(fixed_image.dtype)
print(fixed_image[100,200],"\n")

# GREY COLOR 
print("Grey Color")
print(grey_image.shape)
print(grey_image.dtype)
print(grey_image[100,200], "\n")
print(f"Bgr To grey{grey_image[100,200]}, Manuel: {grey_image1[100,200]}")
print(f"Fark: {cv2.absdiff(grey_image, grey_image1).max()}\n")

# Threshold 
print("Threshold Values")
print(f"Thres1: {thres}, Thresh2: {thres1}, Thres3: {thres2}")

# Total black pixel
print(np.sum(grey_image == 0))

#### Image shows
cv2.imshow("Medal of Honor", image)
cv2.imshow("RGB Medal Of Honor", fixed_image)

cv2.imshow("Grey Medal of Honor", grey_image)
cv2.imshow("Grey Medal of Honor 1", grey_image1)

cv2.imshow("Blue canal", b)
cv2.imshow("Green canal", g)
cv2.imshow("Red canal", r)

cv2.imshow("Painted Image", image_copy)

cv2.imshow("Threshold Image(50)", image_thres)
cv2.imshow("Threshold Image(127)", image_thres1)
cv2.imshow("Threshold Image(200)", image_thres2)

cv2.imshow("Lighted Image", added_image)
cv2.imshow("Darkened Image", subtract_image)

cv2.imshow("Mask 30- 60", masked_image)
cv2.imshow("Mask 120- 170", masked_image1)
cv2.imshow("Mask 200- 250", masked_image2)

cv2.imshow("Blurred (5x5)", blurred_image)
cv2.imshow("Blurred (10x10)", blurred_image1)
cv2.imshow("Blurred (20x20)", blurred_image2)
cv2.imshow("Grey Blurred", grey_blurred_image)
cv2.imshow("Blurred grey", blurred_grey_image)

### histogram 
plt.yscale("log")
plt.axvline(thres, color="red")
plt.axvline(thres1, color="green")
plt.axvline(thres2, color="yellow")
plt.hist(grey_image.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
