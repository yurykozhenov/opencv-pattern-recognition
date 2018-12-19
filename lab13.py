import cv2
import numpy as np
from math import sqrt


def lab13(file_path):
    threshold = 85

    img = cv2.imread(file_path)
    height, width = img.shape[:2]

    # Sobel
    sobel_horizontal = cv2.cvtColor(
        cv2.Sobel(img, -1, 1, 0, ksize=3), cv2.COLOR_BGR2GRAY)
    sobel_vertical = cv2.cvtColor(
        cv2.Sobel(img, -1, 0, 1, ksize=3), cv2.COLOR_BGR2GRAY)

    combined_sobel = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)

    for y in range(height):
        for x in range(width):
            combined_sobel[x][y] = sqrt(
                sobel_horizontal[x][y] ** 2 + sobel_vertical[x][y] ** 2)

    _, combined_sobel_binary = cv2.threshold(
        combined_sobel, threshold, 255, cv2.THRESH_BINARY)

    # Canny
    canny = cv2.Canny(img, threshold, 255)

    # Contours tracing
    _, contours, _ = cv2.findContours(
        canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_L1)
    contours_img = cv2.drawContours(img.copy(), contours, -1, (255, 255, 0))

    cv2.imshow("Original", img)
    cv2.imshow("Sobel Horizontal", sobel_horizontal)
    cv2.imshow("Sobel Vertical", sobel_vertical)
    cv2.imshow("Combined Sobel", combined_sobel)
    cv2.imshow("Combined Sobel (binary)", combined_sobel_binary)
    cv2.imshow("Canny", canny)
    cv2.imshow("Contours tracing", contours_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    lab13("assets/lenna.png")
