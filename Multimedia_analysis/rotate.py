import numpy as np
import matplotlib.pyplot as plt
import cv2

angle = 30*np.pi/180
img = cv2.imread('IMG_0129.jpeg',0)
# img_size
h,w = img.shape[0],img.shape[1]
newW = int(w*abs(np.cos(angle)) + h*abs(np.sin(angle)))+1
newH = int(w*abs(np.sin(angle)) + h*abs(np.cos(angle)))+1
# Attention dtype
newimg1 = np.zeros((newH,newW,3),dtype = int)
newimg2 =  np.zeros((newH,newW,3),dtype = int)
newimg3 =  np.zeros((newH,newW,3),dtype = int)
# scr -> dex
trans1 = np.array([[1,0,0],[0,-1,0],[-0.5*w,0.5*h,1]])
trans1 = trans1.dot(np.array([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,1]]))
trans1 = trans1.dot(np.array([[1,0,0],[0,-1,0],[0.5*newW,0.5*newH,1]]))
# des -> src
trans2 = np.array([[1,0,0],[0,-1,0],[-0.5*newW,0.5*newH,1]])
trans2 = trans2.dot(np.array([[np.cos(angle),np.sin(angle),0],[-np.sin(angle),np.cos(angle),0],[0,0,1]]))
trans2 = trans2.dot(np.array([[1,0,0],[0,-1,0],[0.5*w,0.5*h,1]]))

for x in range(w):
    for y in range(h):
        newPos = np.array([x,y,1]).dot(trans1)
        newimg1[int(newPos[1])][int(newPos[0])] = img[y][x]

for x in range(newW):
    for y in range(newH):
        srcPos = np.array([x,y,1]).dot(trans2)
        if srcPos[0] >= 0 and srcPos[0] < w and srcPos[1] >= 0 and srcPos[1] < h:
            # NN
            newimg2[y][x] = img[int(srcPos[1])][int(srcPos[0])]
            # Bilinear
            bix,biy = int(srcPos[0]),int(srcPos[1])
            if bix < w-1 and biy < h-1:
                rgbX1 = img[biy][bix] + (img[biy][bix+1] - img[biy][bix])*(srcPos[0]-bix)
                rgbX2 = img[biy+1][bix] + (img[biy+1][bix+1] - img[biy+1][bix])*(srcPos[0]-bix)
                rgb = rgbX1 + (rgbX2-rgbX1)*(srcPos[1]-biy)
                newimg3[y][x] = rgb

# plot img
sub = plt.subplot(2,2,1)
sub.set_title("Src Img")
plt.imshow(img)
sub = plt.subplot(2,2,2)
sub.set_title("Src->Des")
plt.imshow(newimg1)
sub = plt.subplot(2,2,3)
sub.set_title("Des->Src & Nearest")
plt.imshow(newimg2)
sub = plt.subplot(2,2,4)
sub.set_title("Des->Src & Bilinear")
plt.imshow(newimg3)
plt.show()
