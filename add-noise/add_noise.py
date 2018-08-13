
import cv2
import numpy as np
import os

def addGausianNosie(src,means,sigma):
    noise = np.random.normal(means,sigma,size=src.shape)
    GaussianImg = src + noise
    return GaussianImg

dir = 'Gray/'
files = os.listdir(dir)
for file in files:
    img = cv2.imread(dir+file)
    for index in range(10):
        res = addGausianNosie(img,0,10)
        cv2.imwrite('Gaussian/'+file[0]+'_'+str(index)+'.png',res)
