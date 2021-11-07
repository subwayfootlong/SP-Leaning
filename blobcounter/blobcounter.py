import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from skimage.color import rgb2hsv, hsv2rgb
import cv2

#Get image input
image_input = imread('testerbutred.png')

#If not red pixel, set to black
red_filtered = (image_input[:,:,0] > 150) & (image_input[:,:,1] < 100) & (image_input[:,:,2] < 110)
plt.figure(num=None, figsize=(8, 6), dpi=80)
image_filtered = image_input.copy()
image_filtered[:, :, 0] = image_filtered[:, :, 0] * red_filtered
image_filtered[:, :, 1] = image_filtered[:, :, 1] * red_filtered
image_filtered[:, :, 2] = image_filtered[:, :, 2] * red_filtered

#change red pixels to white
image_filtered[np.where((image_filtered==[255,0,0]).all(axis=2))] = [255, 255, 255]

#blob counting
image = image_filtered
mask = np.zeros(image.shape, dtype=np.uint8)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
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


#cv2.imshow('thresh', thresh)
#cv2.imshow('opening', opening)
#cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.waitKey()
