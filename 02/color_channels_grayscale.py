"""
Разделение на цветовые каналы и преобразование в полутоновое
Демонстрирует:
- разделение изображения на каналы BGR
- два способа преобразования в grayscale (ручной и встроенный)
- сравнение результатов
"""
import cv2
import numpy as np

image = cv2.imread('img/Birds.jpg')

cv2.imshow('original', image)
cv2.waitKey(0)

b, g, r = cv2.split(image)

# Ручное преобразование в grayscale с использованием коэффициентов
rows, cols, ch = image.shape
gray1 = np.zeros((rows, cols), np.uint8)

for y in range(0, rows):
    for x in range(0, cols):
        gray1[y, x] = np.uint8(
            min(255, 0.299 * r[y, x] + 0.587 * g[y, x] + 0.114 * b[y, x]))

cv2.namedWindow('grayscale1', cv2.WINDOW_NORMAL)
cv2.imshow('grayscale1', gray1)
cv2.waitKey(0)

# Автоматическое преобразование в grayscale средствами OpenCV
gray2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('grayscale2', cv2.WINDOW_NORMAL)
cv2.imshow('grayscale2', gray2)
cv2.waitKey(0)

# Сравнение двух методов преобразования
dif = np.zeros((rows, cols), np.uint8)
dif = np.uint8(abs(np.subtract(np.double(gray2), np.double(gray1))))

cv2.namedWindow('difference', cv2.WINDOW_NORMAL)
cv2.imshow('difference', dif)
cv2.waitKey(0)

cv2.destroyAllWindows()
