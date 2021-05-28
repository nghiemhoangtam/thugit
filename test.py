import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('digits.png',0)
cv2.imshow('sa',img)

cells = [np.hsplit(row,100) for row in np.vsplit(img,50)]
# print(cells[0][5])
print(img.shape)
cv2.imwrite('so.jpg',cells[1][1])
img2=cv2.imread('so.jpg')
cv2.imshow('so',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()