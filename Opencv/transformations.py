import cv2 as cv
import numpy as np

img = cv.imread('Opencv/photos/cat.jpeg')
cv.imshow('cat',img)

def translate(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dim =(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dim)

trans=translate(img,100,100)
cv.imshow('transs',trans)

cv.waitKey(0)