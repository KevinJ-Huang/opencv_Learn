import cv2
import argparse
import numpy as np


def main(args):
    img = cv2.imread(args.file)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    channels = cv2.split(hsv)
    channels[1] = 255*np.ones([img.shape[0],img.shape[1]]).astype(np.uint8)
    channels[2] = 200*np.ones([img.shape[0],img.shape[1]]).astype(np.uint8)
    hsv = cv2.merge(channels)
    rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    cv2.imshow('image',rgb)
    cv2.waitKey(0)



if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file",default="test.png",help="Image that input")
    args = parser.parse_args()
    main(args)