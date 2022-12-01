# Edge Detection
import cv2
import numpy as np
from matplotlib import pyplot as plt
i=cv2.imread('lena.jpg')
plt.figure(figsize=(20, 20))
laplacian=cv2.Laplacian(i,cv2.CV_64F)
canny=cv2.Canny(i, 150, 250)
SX=cv2.Sobel(i,cv2.CV_64F,1,0,ksize=5)
SY=cv2.Sobel(i,cv2.CV_64F,0,1,ksize=5)
l=[i,laplacian,canny,SX,SY]
t=["Original","Laplacian","Canny","Sobel X","Sobel Y"]
for i in range(5):
 cv2.imshow(t[i],l[i]) 
cv2.waitKey(0) 
cv2.destroyAllWindows()