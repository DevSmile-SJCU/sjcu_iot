import cv2
import numpy as np
 
imageFile = './data/lena.jpg'
img = cv2.imread(imageFile)
cv2.imshow('Lena Original',img)

# 선과 사각형 그리기 
pt1 = 100, 100
pt2 = 300, 300
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)

cv2.line(img, (0, 0), (400, 0), (255, 0, 0), 10)
cv2.line(img, (0, 0), (0, 400), (0,0,255), 10)

# 특정 영역의 색상 변경
img[10:50, 10:50] = 0

# 텍스트 출력
font = cv2.FONT_HERSHEY_SIMPLEX
text = "Hello IoT"
cv2.putText(img, text, (300, 300), font, 1, (255, 255, 255), 4)

cv2.imshow('Lena Edited',img)
cv2.imwrite('./data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 2])
 
imageFile = './data/Lena2.jpg'
img  = cv2.imread(imageFile)
cv2.imshow('Lena 2nd',img)
 
cv2.waitKey()
cv2.destroyAllWindows()