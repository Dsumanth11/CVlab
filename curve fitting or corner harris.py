import cv2
import numpy as np
from matplotlib import pyplot as plt
i=cv2.imread('lena.jpg')
gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
i1=np.float32(gray)
res=cv2.cornerHarris(i1,2,5,0.07)
res=cv2.dilate(res, None)
i[res>0.01*res.max()]=[0,0,255]
plt.imshow(i)
plt.title("Detected corners")
plt.xticks([]),plt.yticks([])
plt.show()