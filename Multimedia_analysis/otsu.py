
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

 g = np.zeros(256, np.float)

for i in range(0, height):
    for j in range(0, width):
        pixel = img[i,j]
        index = int(pixel)
        count[index] = count[index]+1

for i in range(0, 256):
    count_ratio[i] = count[i]/(height*width)


def sum_fromi2j(array, i, j):
    sum = 0
    for n in range(i,j):
        sum = sum + array[n]
    return sum

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


 for i in range(0,256):
    
    w0 = sum_fromi2j(count_ratio, 0, i)
    u0 = mean_fromi2j(count, 0, i)
    
    w1 = sum_fromi2j(count_ratio, i, 255)
    u1 = mean_fromi2j(count, i, 255)
    
    g[i] = w0*w1*(np.power(u0-u1, 2))


index = np.where(g == np.max(g))

for i in range(0, height):
    for j in range(0, width):
        if img[i, j]>=index:
            img[i, j] = 255
        else:
            img[i, j] = 0

cv2.imwrite('IMG_SHOGI1.jpeg', img, [cv2.IMWRITE_JPEG_QUALITY,80])






