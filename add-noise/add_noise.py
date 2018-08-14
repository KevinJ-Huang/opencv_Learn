
import cv2
import numpy as np
import os

def addGausianNosie(src,means,sigma):
    noise = np.random.normal(means,sigma,size=src.shape)
    GaussianImg = src + noise
    GaussianImg_clip = np.clip(GaussianImg,0,255)
    return GaussianImg_clip

dir = '/root/hj9/images/Gray_train/'
files = os.listdir(dir)
for file in files:
    img = cv2.imread(dir+file)
    for index in range(1700):
        res = addGausianNosie(img,0,10)
        cv2.imwrite('/root/hj9/images/train/'+file[0:-4]+'_'+str(index)+'.jpg',res)
