import cv2
import numpy as np


def lab12(file_path):
    min_rect_dim = 470
    max_rect_dim = 540
    threshold = 235

    img = cv2.imread(file_path)

    _, dst = cv2.threshold(cv2.cvtColor(
        img, cv2.COLOR_BGR2GRAY), threshold, 255, cv2.THRESH_BINARY_INV)

    for y in range(len(dst)):
        for x in range(len(dst[0])):
            value = dst[y][x]

            if value == 255:
                count, _, _, rect = cv2.floodFill(dst, None, (x, y), 200)

                x = rect[0]
                y = rect[1]
                width = rect[2]
                height = rect[3]

                if width >= min_rect_dim and width <= max_rect_dim and height >= min_rect_dim and height <= max_rect_dim:
                    x1 = x + width // 2
                    y1 = y + height // 2
                    rad = (width + height) // 4
                    cv2.circle(img, (x1, y1), rad, (255, 0, 255), 2)

    cv2.imshow("Original", img)
    cv2.imshow("Threshold", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    lab12("assets/oranges.jpg",)
