# morphological operations
import cv2
import numpy as np
from matplotlib import pyplot as plt
kernel=np.ones((5,5),np.uint8)
i=cv2.imread('lena.jpg')
_,mask = cv2.threshold(i,150,255,cv2.THRESH_BINARY)
erosion=cv2.erode(i,kernel,iterations=1)
dilation=cv2.dilate(i,kernel,iterations=1)
opening=cv2.morphologyEx(i,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(i,cv2.MORPH_CLOSE,kernel)
l=[i,erosion,dilation,opening,closing,mask]
t=["Original","Erosion","Dilation","Opening","Closing","Mask"]
for i in range(5):
 cv2.imshow(t[i],l[i]) 
cv2.waitKey(0) 
cv2.destroyAllWindows()