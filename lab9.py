import cv2


def lab9(file_path):
    img = cv2.imread(file_path)

    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    lab9("assets/lenna.png")
