import cv2
import numpy as np
import math
import time

img = cv2.imread("router.jpg")
height, width = img.shape[:2]

# Perspective transform
a = [31, 351]
b = [387, 207]
c = [571 ,460]
d = [158, 673]

src = np.float32([a, b, c, d])
dst = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
transform = cv2.getPerspectiveTransform(src, dst)
persp = cv2.warpPerspective(img, transform, img.shape[1::-1])

cv2.imshow("Original", img)

param_mult_1 = 1.4
param_mult_2 = 2.3
param_mult_3 = 0.5
param_mult_4 = 0.9

param_add_1 = 100
param_add_2 = 750

# Bilinear transform
while True:
        map_x = np.zeros((img.shape[0], img.shape[1]), dtype=np.float32)
        map_y = np.zeros((img.shape[0], img.shape[1]), dtype=np.float32)

        for i in range(map_x.shape[0]):
                for j in range(map_x.shape[1]):
                        map_x[i, j] = param_mult_1 * j - param_mult_3 * i + param_add_1
                        map_y[i, j] = param_mult_2 * i + param_mult_4 * j - param_add_2

        remaped = cv2.remap(persp, map_x, map_y, cv2.INTER_LINEAR)
        cv2.imshow("Bilinear transform", remaped)
        key = cv2.waitKey(0)

        if key == 97:
                param_mult_1 += 0.1
        if key == 100:
                param_mult_1 -= 0.1
        if key == 115:
                param_mult_2 += 0.1
        if key == 119:
                param_mult_2 -= 0.1
        if key == 105:
                param_mult_3 += 0.1
        if key == 107:
                param_mult_3 -= 0.1
        if key == 106:
                param_mult_4 += 0.1
        if key == 108:
                param_mult_4 -= 0.1

        # param_add_1 += 100  
        param_add_2 += 100
        print(param_mult_1, param_mult_2, param_mult_3, param_mult_4, param_add_1, param_add_2)


cv2.destroyAllWindows()
