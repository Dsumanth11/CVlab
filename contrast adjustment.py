import cv2
from matplotlib import pyplot as plt
from PIL import Image,ImageEnhance
plt.figure(figsize=(30,30))
i=Image.open('lena.jpg')
lcv=0.1
mcv=1
hcv=2
original=ImageEnhance.Contrast(i)
i1=original.enhance(lcv)
i2=original.enhance(mcv)
i3=original.enhance(hcv)
l=[i,i1,i2,i3]
t=["Original","Low Contrast","Medium Contrast","High Contrast"]
for i in range(4):
 plt.subplot(4,4,i+1)
 plt.imshow(l[i])
 plt.title(t[i])
 plt.xticks([]),plt.yticks([])
plt.show() 