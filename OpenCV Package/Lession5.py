import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    img = cv2.line(frame,(0,0),(width , height),(0,0,0),5)

    img = cv2.rectangle(frame , (100 , 100) , (200 , 400) , (255 , 200 , 55) ,1)

    img = cv2.circle(frame , (150 , 150) , 70 , (255 , 125 , 24) , -1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(frame , "Nguyen Hong Minh" , (200 , 400) , 2, 1.2 , (255 , 255 , 255) , 1 )
    cv2.imshow("Cua so" , frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
