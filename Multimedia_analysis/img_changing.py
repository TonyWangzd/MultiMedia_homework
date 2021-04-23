import cv2
# info
# create a blank pattern
# calculate the x and y
import numpy as np


img = cv2.imread('IMG_0122.jpeg',1)# read a image  1: name 2 : 0 gray 1 color

####### expansion ###########


img_Info = img.shape
img_height = img_Info[0]
img_width = img_Info[1]
print(img_height)

dst_height = int(img_height*0.5)
dst_width = int(img_width*0.5)
dst_img = np.zeros((dst_height,dst_width,3), np.uint8) #0-255


for i in range(0, dst_height):
    for j in range(0, dst_width):
        i_new = int(i*(img_height*1.0/dst_height))
        j_new = int(j*(img_width*1.0/dst_width))
        dst_img[i, j] = img[i_new, j_new]
   

cv2.imwrite('IMG_0126.jpeg', dst_img, [cv2.IMWRITE_JPEG_QUALITY,80])

######## sampling #############

dst2_img = np.zeros((dst_height, dst_width ,3), np.uint8)
sampling_bit  = 8  #change with number in 2, 4, 8, 16, 32, 64, 128, 256
color_array = []
number = 0

for i in range(0, sampling_bit+1):
    color_array.append(number)
    number = number + 256/sampling_bit

half = (256/sampling_bit)/2

for i in range(0, dst_height):
    for j in range(0, dst_width):
        color = dst_img[i, j]
        new_color = []
        for number in range(3):
            for level in color_array:
                if (color[number] < level+half*2) and (level < color[number]):
                    if ((color[number]-level) < half):
                        dst2_img[i, j][number] = level
                    else:
                        dst2_img[i, j][number] = level+half
                    print(dst2_img[i, j][number],number,i,j)


cv2.imwrite('IMG_0128.jpeg', dst2_img, [cv2.IMWRITE_JPEG_QUALITY,100])






