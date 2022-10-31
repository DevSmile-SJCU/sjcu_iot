import cv2
import numpy as np
 
imageFile = './data/lena.jpg'
img = cv2.imread(imageFile)
cv2.imshow('Lena color',img)

cv2.imwrite('./data/Lena.bmp', img)
cv2.imwrite('./data/Lena.png', img)
cv2.imwrite('./data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
 
imageFile = './data/Lena.png'
img  = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Lena gray',img)
 
cv2.waitKey()
cv2.destroyAllWindows()