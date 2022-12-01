import cv2
img = cv2.imread("lena.jpg")
cv2.imshow("Input Image",img)
 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30, minRadius = 0, maxRadius = 0)
 
for circle in circles[0,:]:
    cv2.circle(img,(int(circle[0]),int(circle[1])), int(circle[2]), (220,255,0), 3)
 
cv2.imshow("hough transform",img)
cv2.waitKey(0)
cv2.destroyAllWindows()