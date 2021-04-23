
#!/usr/bin/env python
# -*- coding: utf-8 -*-import cv2
import numpy as np
import matplotlib.pyplot as plt
import cv2


img = cv2.imread('IMG_shogi.jpg',0)
img_info = img.shape

height = img_info[0]
width = img_info[1]

count = np.zeros(256, np.float)
count_ratio = np.zeros(256, np.float)

for i in range(0, height):
    for j in range(0, width):
        pixel = img[i,j]
        index = int(pixel)
        count[index] = count[index]+1

for i in range(0, 256):
    count_ratio[i] = count[i]/(height*width)


def mean_fromi2j(array, i, j):
    sum_pixel = 0
    sum = 0
    for n in range(i, j):
        sum_pixel = sum_pixel + array[n] * n
        sum = sum + array[n]
    if (sum != 0):
        mean = float(sum_pixel/sum)
    else:
        mean = 0
    
    return mean

for i in range(0, 256):
    if count[i] != 0:
        min = i
        print('the minist number is ',min)
        break


for i in range(0,255):
    if count[255-i] != 0:
        max = 255-i
        print('the max number is ', max)
        break

T = int((max + min) / 2)

T_changed = True

while(T_changed):
    oldT = T
    zo = mean_fromi2j(count, 0, T)
    zb = mean_fromi2j(count, T, 255)
    T = int((zo + zb)/2)
    if oldT == T:
        T_changed = False

index = T

for i in range(0, height):
    for j in range(0, width):
        if img[i, j]>=index:
            img[i, j] = 255
        else:
            img[i, j] = 0

cv2.imwrite('IMG_SHOGI1.jpeg', img, [cv2.IMWRITE_JPEG_QUALITY,80])
        


