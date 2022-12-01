import cv2
import numpy as np
i=cv2.imread('lena.jpg')
a=np.array(i)
print("sum of img :",np.sum(a))
print("mean of img :",np.mean(a))
print("min of img :",np.min(a))
print("max of img :",np.max(a))
print("variance of img :",np.var(a))
print("standard deviation of img :",np.std(a))
cv2.imshow('original image',i)
cv2.waitKey(0)
cv2.destroyAllWindows()