import cv2
from matplotlib import pyplot as plt
plt.figure(figsize=(10, 10))
img = cv2.imread('lena.jpg')
org=img.copy()
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray,10,100)
contours,hierarchy=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours,-1,(0,0,255),2)
l=[org,img]
t=["Original","Image With Contours"]
for i in range(2):
 cv2.imshow(t[i],l[i]) 
cv2.waitKey(0) 
cv2.destroyAllWindows()