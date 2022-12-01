import cv2
import numpy as np
from matplotlib import pyplot as plt
plt.figure(figsize=(20, 20))
img=cv2.imread("lena.jpg")
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img=img.astype(np.float64)/255
c,m,y=(1-img[...,2]),(1-img[...,1]),(1-img[...,0])
cmy=(np.dstack((c,m,y))*255).astype(np.int8)
l=[img,hsv,cmy]
t=["Original","HSV","CMY"]
for i in range(3):
 cv2.imshow(t[i],l[i]) 
cv2.waitKey(0) 
cv2.destroyAllWindows()