import cv2
from matplotlib import pyplot as plt


def lab10(file_path):
    img = cv2.imread(file_path, 0)

    # Manual histogram
    hist = [0] * 256

    for row in img:
        for col in row:
            hist[col] += 1

    plt.bar(range(256), hist, label="Original (manual)")

    # Auto histogram
    plt.hist(img.ravel(), 256, [0, 256], label="Original")

    # Normalize
    normalized = img.copy()
    cv2.normalize(img, normalized, 0, 255, cv2.NORM_MINMAX)
    plt.hist(normalized.ravel(), 256, [0, 256], label="Normalized")

    # Equalize
    equalized = img.copy()
    cv2.equalizeHist(img, equalized)
    plt.hist(equalized.ravel(), 256, [0, 256], label="Equalized")

    cv2.imshow("Original", img)
    cv2.imshow("Normalized", normalized)
    cv2.imshow("Equalized", equalized)

    plt.legend(loc="upper right")
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    lab10("assets/lenna.png")
