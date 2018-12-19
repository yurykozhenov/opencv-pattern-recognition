import cv2
import numpy as np


def findSkeleton(file_path):
    original_img = cv2.imread(file_path, 0)
    _, img = cv2.threshold(original_img, 127, 255, cv2.THRESH_BINARY)  # 1

    skeleton = np.zeros(original_img.shape, np.uint8)  # 2

    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    while cv2.countNonZero(img) != 0:
        eroded = cv2.erode(img, kernel)  # 3
        dilated = cv2.dilate(eroded, kernel)  # 4
        difference = cv2.subtract(img, dilated)  # 5

        skeleton = cv2.bitwise_or(skeleton, difference)  # 6
        img = eroded.copy()  # 7

    cv2.imshow("Original", original_img)
    cv2.imshow("Skeleton", skeleton)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    findSkeleton("assets/bit.png")
