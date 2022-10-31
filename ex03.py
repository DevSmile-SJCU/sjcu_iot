# 필요한 Module(Library) 임포트
import numpy as np
import cv2 as cv

# 도로 이미지 읽어서 표시
cimg = cv.imread('./data/road.jpg')
cv.imshow('Roads - original', cimg)

# 도로이미지 이진화, 에지 추출 후 표시
img = cv.cvtColor(cimg, cv.COLOR_BGR2GRAY)
_, img = cv.threshold(img, 170, 255, cv.THRESH_BINARY)
img = cv.Canny(img, 50, 200, None, 3)
cv.imshow('Image - binary & edge', img)

# Harris를 이용한 모서리 검출
k = 0.1
T = 0.01
R = cv.cornerHarris(img, 2, 3, k)

# 원본 이미지 + 모서리 표시
cimg[R > T * R.max()] = [0, 0, 255]
cv.imshow('Harris Coners', cimg)

# 사용자 입력키 대기 및 종료
cv.waitKey()
cv.destroyAllWindows()