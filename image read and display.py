import cv2
import matplotlib.pyplot as plt
img = cv2.imread("lena.jpg")
cv2.imshow("Image", img)
print("Image Properties:")
print("Number of pixels:"+str(img.size))
print("Image dimensions:"+str(img.shape))
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(img)
plt.show()