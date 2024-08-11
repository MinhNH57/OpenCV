import random
import cv2
img = cv2.imread("C:\\Users\\Dell\Pictures\\Screenshots\\Screenshot 2024-06-23 233908.png" , 1)
# cv2.imshow("Img" ,img)
# print(type(img))
print(img[600])
# print(img)
print(img.shape)
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] =[random.randint(0,225),random.randint(0,225),random.randint(0,225)]
cv2.imshow("Img" , img)
vungChon = img[0:200 , 200:400]
img[200:400 ,300:500 ] = vungChon
cv2.imshow("Img" , img)
k = cv2.waitKey()