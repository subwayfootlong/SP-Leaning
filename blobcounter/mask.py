import cv2, os
import numpy as np

#Some Visual Studio Code bullshit because it cant find the image????
os.chdir('C:/Users/lais/Desktop/SP/CIOT/projects/blob')

#Get image input
orig_image = cv2.imread('pic/IMG_6942.jpg')
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

cv2.imshow('image', orig_image)
cv2.imshow('Initial Masking', masked_image)
cv2.waitKey()