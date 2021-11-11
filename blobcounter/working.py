import cv2, os
import numpy as np

#Some Visual Studio Code bullshit because it cant find the image????
os.chdir('C:\Program Files\Python\projects\Blob')

#Get image input
orig_image = cv2.imread("real2.jpg")
image = orig_image.copy()

#Image Masking
# Blur image to get rid of noise
image = cv2.GaussianBlur(image, (3, 3), cv2.BORDER_DEFAULT)
# Convert to hue-saturation-value
h, s, v = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
# "Roll" the hue value so reds (which would otherwise be at 0 and 255) are in the middle instead.
# This makes it easier to use `inRange` without needing to AND masks together.
image = cv2.merge(((h + 128) % 255, s, v))
# Select the correct hues with saturated-enough, bright-enough colors.
masked_image = cv2.inRange(image, np.array([40, 128, 100]), np.array([140, 255, 255]))

#Blob counter
mask = np.zeros(masked_image.shape, dtype=np.uint8)
thresh = cv2.threshold(masked_image,0,255,cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=5)

cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

blobs = 0
for c in cnts:
    area = cv2.contourArea(c)
    cv2.drawContours(mask, [c], -1, (36,255,12), -1)
    if area > 13000:
        blobs += 2
    else:
        blobs += 1

print('blobs:', blobs)

cv2.imshow('image', orig_image)
#cv2.imshow('Initial Masking', masked_image)
#cv2.imshow('mask', mask)
#cv2.imshow('thresh', thresh)
cv2.imshow('opening', opening)
cv2.waitKey()