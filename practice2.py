
import cv2
import numpy as np
import math

# Histogram Equalization
img1 = cv2.imread('input1.png')
dst_img1 = np.zeros(img1.shape, np.uint8)
for i in range(0,3):
    dst_img1[:,:,i] = cv2.equalizeHist(img1[:,:,i])
cv2.imshow("Histogram Equalization",dst_img1)

# Laplacian
img2 = cv2.imread('input2.jpeg')
dst_img2 = np.zeros(img2.shape, np.uint8)
kernel = np.array([[0,-1,0],[0,5,0],[0,-1,0]])
cv2.filter2D(img2,cv2.CV_8UC3,kernel,dst_img2)
cv2.imshow("Laplacian Effect",dst_img2)

# Log transfer
img3 = cv2.imread('input3.jpeg')
dst_img3 = np.zeros(img3.shape, np.float32)
for i in range(0,img3.shape[0]):
    for j in range(0,img3.shape[1]):
        for k in range(0,3):
            dst_img3[i,j,k] = math.log(1+img3[i,j,k])
cv2.normalize(dst_img3,dst_img3,0,255,cv2.NORM_MINMAX)
dst_img3 = np.uint8(dst_img3)
cv2.convertScaleAbs(dst_img3,dst_img3)
cv2.imshow("Log result",dst_img3)
cv2.waitKey(0)
