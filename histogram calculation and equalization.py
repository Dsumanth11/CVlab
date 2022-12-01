import cv2
from matplotlib import pyplot as plt
import numpy as np
i=cv2.imread('lena.jpg',0)
equalize=cv2.equalizeHist(i)
res=np.hstack((i,equalize))
histogram_plot=cv2.calcHist([i],[0],None,[250],[0,256])
cv2.imshow('Image Histogram',res)
plt.plot(histogram_plot)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
