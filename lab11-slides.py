import cv2


def lab11_slides(file_path):
    img = cv2.imread(file_path)

    # Generate 100 slides with gradually increasing blur
    slides = 100
    for num in range(1, slides + 1):
        median = cv2.medianBlur(img, num if num % 2 != 0 else num + 1)
        cv2.imwrite(f"lab11/slides/{num}.bmp", median)


if __name__ == "__main__":
    lab11_slides("assets/lenna.png")
