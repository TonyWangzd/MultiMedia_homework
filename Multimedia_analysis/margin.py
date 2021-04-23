import cv2
import numpy as np

img = cv2.imread('IMG_marshall.jpeg',0)

img_info = img.shape
height, width = img_info[0],img_info[1]

dst = np.zeros((height,width,1),np.uint8)

for i in range(0, height):
    for j in range(0,width-1):
        imgP0 = int(img[i,j])
        imgP1 = int(img[i,j+1])
        newP = imgP0 - imgP1 + 150
        if newP > 255:
            newP = 255
        if newP < 0:
            newP = 0
        dst[i,j] = newP

cv2.imwrite('IMG_MARSHALL_MARGIN.jpeg',dst,[cv2.IMWRITE_JPEG_QUALITY,90])