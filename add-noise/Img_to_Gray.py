import cv2
import os

dir = 'Input/'
files = os.listdir(dir)
index = 1
for file in files:
    img = cv2.imread(dir+file,0)
    cv2.imwrite('Gray/'+str(index)+'.png',img)
    index+=1
