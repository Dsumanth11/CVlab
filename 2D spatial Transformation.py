import cv2
from matplotlib import pyplot as plt
plt.figure(figsize=(30,30))
img = cv2.imread("lena.jpg")
resize = cv2.resize(img,(80,60))
height,width = img.shape[:2]
center = (width/2, height/2)
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=65, scale=1)
rotated = cv2.warpAffine(src = img, M=rotate_matrix,dsize=(width,height))
l=[img,resize,rotated]
t=["Original","Resize","Rotated"]
for i in range(3):
 plt.subplot(1,3,i+1)
 plt.imshow(l[i])
 plt.title(t[i])
 plt.xticks([]),plt.yticks([])
plt.show() 
