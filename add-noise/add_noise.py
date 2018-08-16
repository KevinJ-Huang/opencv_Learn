import cv2
import numpy as np
import os
from PIL import Image

def addGausianNosie(src,means,sigma):
    src = np.array(src)
    x = src.shape[0]
    y = src.shape[1]
    noise = means+sigma * np.random.randn(x,y)
    GaussianImg = src + noise
    GaussianImg_clip = np.clip(GaussianImg,0,255)
    return GaussianImg_clip

dir = '/root/hj9/images2/train_gt/'
files = os.listdir(dir)
for file in files:
    img = Image.open(dir+file)
    for index in range(1700):
        res = addGausianNosie(img,0,10)
        res = Image.fromarray(res)
        res = res.convert('L')
        # res.save('/root/hj9/images2/val_noise/'+file)
        res.save('/root/hj9/images2/train_noise/' + file[0:-4]+'_'+str(index)+'.jpg')
