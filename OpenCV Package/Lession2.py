import cv2

img = cv2.imread("C:\\Users\\Dell\\Pictures\\Screenshots\\Screenshot 2024-06-23 233908.png")
# img = cv2.resize(img , (400 , 400))
img = cv2.resize(img , (0,0) , fx=0.5 , fy=0.5)
img1 = cv2.rotate(img , cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Img", img1)
k = cv2.waitKey(0)