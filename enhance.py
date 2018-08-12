import cv2
import argparse
import numpy as np


def main(args):
    img = cv2.imread(args.file)
    img2 = np.zeros(shape=img.shape)
    for i in range(0,img.shape[0]):
        for j in range(0, img.shape[1]):
            for k in range(0, img.shape[2]):
                img2[i, j, k] = 255 - img[i, j, k]

    img3 = np.zeros(shape=img.shape)
    for i in range(0,img.shape[0]):
        for j in range(0, img.shape[1]):
            for k in range(0, img.shape[2]):
                img3[i, j, k] = 255 - 100*img2[i , j, k]

    cv2.imshow('image',img3)
    cv2.imwrite('result.png',img3)
    cv2.waitKey(0)



if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file",default="test1.png",help="Image that input")
    args = parser.parse_args()
    main(args)