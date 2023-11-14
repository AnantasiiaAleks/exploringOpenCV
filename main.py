import cv2

img = cv2.imread('test.jpg')

#print(img)

#img = cv2.resize(img, (500, 500))  #изменить размер

print(img.shape) #напечатать размер картинки

cv2.imshow('Result', img)

cv2.waitKey(0)