import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('IMG_marshall.jpeg',0)
img_info = img.shape
height = img_info[0]
width = img_info[1]

################################

count = np.zeros(256,np.float)

for i in range(0, height):
    for j in range(0, width):
        pixel = img[i,j]
        index = int(pixel)
        count[index] = count[index]+1

for i in range(0, 255):
    count[i] = count[i]/(height*width)

x = np.linspace(0, 255, 256)
y = count

for i in range(0, 255):
    if count[i] != 0:
        min = i
        print('the minist number is ',min)
        break

for i in range(0,255):
    if count[255-i] != 0:
        max = 255-i
        print('the max number is ', max)
        break

dst_img = np.zeros((height,width), np.uint8) #0-255
for i in range(0, height):
    for j in range(0, width):
        dst_img[i,j] = ((img[i,j]-min)/(max-min))*255
       
def histogram(img):
    img_info = img.shape
    height = img_info[0]
    width = img_info[1]
    count = np.zeros(256,np.float)
    
    for i in range(0, height):
        for j in range(0, width):
            pixel = img[i,j]
            index = int(pixel)
            count[index] = count[index]+1
            
    for i in range(0, 255):
        count[i] = count[i]/(height*width)
    
    x = np.linspace(0, 255, 256)
    y = count
    plt.bar(x, y, 0.9, alpha=1, color='b')


histogram(dst_img)
histogram(img)

#2
sum1 = float(0)
count2 = np.zeros(256,float)

for i in range(0, height):
    for j in range(0, width):
        pixel = img[i,j]
        index = int(pixel)
        count2[index] = count2[index]+1


for i in range(0, 255):
    count2[i] = count2[i]/(height*width)


sum1 = float(0)
for i in range(0, 255):
    sum1 = count2[i]+sum1
    count2[i] = sum1


#calculate mapping
mapping = np.zeros(256, np.uint16)
for i in range(0, 256):
    mapping[i] = count2[i]*255
#mapping
dst_img2 = np.zeros((height,width), np.uint8)
for i in range(0, height):
    for j in range(0, width):
        dst_img2[i,j] = mapping[img[i,j]]

histogram(dst_img2)

#save img
cv2.imwrite('IMG_MARSHALL2.jpeg', dst_img2, [cv2.IMWRITE_JPEG_QUALITY,80])
cv2.imwrite('IMG_MARSHALL1.jpeg', dst_img, [cv2.IMWRITE_JPEG_QUALITY,80])




