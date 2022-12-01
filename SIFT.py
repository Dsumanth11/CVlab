import numpy as np
import cv2
i=cv2.imread("lena.jpg")
gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
sift=cv2.SIFT_create()
detect=sift.detect(gray,None)
i=cv2.drawKeypoints(gray,detect,i)
cv2.imshow('Output',i)
cv2.waitKey(0)
cv2.destroyAllWindows()