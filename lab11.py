import cv2
import numpy as np
import math


def lab11(file_path):
    img = cv2.imread(file_path)
    height, width = img.shape[:2]

    # Perspective transform
    a = [31, 351]
    b = [387, 207]
    c = [571, 460]
    d = [158, 673]

    src = np.float32([a, b, c, d])
    dst = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    transform = cv2.getPerspectiveTransform(src, dst)
    persp = cv2.warpPerspective(img, transform, img.shape[1::-1])

    # Bilinear transform
    map_x = np.zeros((img.shape[0], img.shape[1]), dtype=np.float32)
    map_y = np.zeros((img.shape[0], img.shape[1]), dtype=np.float32)

    for i in range(map_x.shape[0]):
        for j in range(map_x.shape[1]):
            map_x[i, j] = 1.4 * j - 0.5 * i + 100
            map_y[i, j] = 2.3 * i + 0.9 * j - 750

    remaped = cv2.remap(persp, map_x, map_y, cv2.INTER_LINEAR)

    # Morphological operations
    ker = np.ones((5, 5), "uint8")

    # Erosion
    erosion = cv2.erode(img, ker, iterations=1)

    # Dilation
    dilation = cv2.dilate(img, ker, iterations=1)

    # Opening
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, ker)

    # Closing
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, ker)

    cv2.imshow("Original", img)
    cv2.imshow("Perspective transform", persp)
    cv2.imshow("Bilinear transform", remaped)
    cv2.imshow("Erosion", erosion)
    cv2.imshow("Dilation", dilation)
    cv2.imshow("Opening", opening)
    cv2.imshow("Closing", closing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    lab11("assets/router.jpg")
