import cv2
from matplotlib import pyplot as plt
i=cv2.imread('lena.jpg')
g=cv2.GaussianBlur(i,(5,5),0)
m=cv2.medianBlur(i,7)
bi=cv2.bilateralFilter(i,7,75,75)
box=cv2.boxFilter(i,0,(7,7),(-1,-1))
l=[i,g,m,bi,box]
t=["Original","GaussianBlur","MedianBlur","BilateralFilter","BoxFilter"]
for i in range(5):
 cv2.imshow(t[i],l[i]) 
cv2.waitKey(0) 
cv2.destroyAllWindows()