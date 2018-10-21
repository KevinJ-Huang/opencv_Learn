from skimage.transform import resize
import cv2
import random

img = cv2.imread('input1/a0001.jpg')


def speify_resize(img,size=512):
    w, h = img.shape[:2]
    if w < h:
        width, height = (size, int(size*h / w ))
    else:
        width, height = (int(size*w / h ), size)
    img = resize(img, (int(width), int(height)), mode='reflect')
    return img

def random_resize(img):
    w, h = img.shape[:2]
    size_seed = [512,768,1024,1280,1536]
    id = random.randint(0,4)
    size = size_seed[id]
    if w < h:
        width, height = (size, int(size*h / w ))
    else:
        width, height = (int(size*w / h ), size)
    img = resize(img, (int(width), int(height)), mode='reflect')
    return img

img = random_resize(img)


print(img.shape)
