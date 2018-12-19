import cv2
from matplotlib import pyplot as plt

img = cv2.imread("lenna.png", 0)

# Manual histogram
hist = [0] * 256

for row in img:
    for col in row:
        hist[col] += 1

plt.bar(range(0, 255), hist, label="Original (manual)")

# Auto histogram
plt.hist(img.ravel(), 256, [0, 256], label="Original")

# Auto normalize
normalized = img.copy()
cv2.normalize(img, normalized, 0, 255, cv2.NORM_MINMAX)
plt.hist(normalized.ravel(), 256, [0, 256], label="Normalized")

# Manual normalize
normalizedManual = img.copy()
minColor = min(img.ravel())
maxColor = max(img.ravel())

for rowIndex, row in enumerate(normalizedManual):
    for colIndex, col in enumerate(row):
        normalizedManual[rowIndex][colIndex] = 255 * ((col - minColor) / (maxColor - minColor))

plt.hist(normalizedManual.ravel(), 256, [0, 256], label="Normalized (manual)")

# Equalize
equalized = img.copy()
cv2.equalizeHist(img, equalized)
plt.hist(equalized.ravel(), 256, [0, 256], label="Equalized")

cv2.imshow("Original", img)
cv2.imshow("Normalized", normalized)
cv2.imshow("Normalized (manual)", normalized)
cv2.imshow("Equalized", equalized)

plt.legend(loc="upper right")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
