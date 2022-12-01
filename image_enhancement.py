# Image Enhancement.
import cv2
from PIL import Image,ImageEnhance
from matplotlib import pyplot as plt
i=Image.open('lena.jpg')
NBV=NCV=NSV=NKV=1.5
a=ImageEnhance.Brightness(i)
NB=a.enhance(NBV)
b=ImageEnhance.Sharpness(i)
NS=b.enhance(NSV)
c=ImageEnhance.Contrast(i)
NC=c.enhance(NCV)
d=ImageEnhance.Color(i)
NK=d.enhance(NKV)
l=[i,NB,NK,NC,NS]
t = ['Original','Brightness','Color','Contrast','Sharpness']
for i in range(5):
 plt.subplot(2,3,i+1)
 plt.imshow(l[i])
 plt.title(t[i])
 plt.xticks([]),plt.yticks([])
plt.show()