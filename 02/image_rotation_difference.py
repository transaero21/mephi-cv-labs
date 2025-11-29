"""
Аффинные преобразования и разность изображений
Демонстрирует:
- поворот изображения с использованием матрицы преобразования
- вычисление разности между изображениями
- масштабирование разности для визуализации
"""
import cv2
import numpy as np

img1 = cv2.imread('img/Birds.jpg')

cv2.imshow('Original', img1)
cv2.waitKey(0)

rows, cols, r = img1.shape

# Поворот изображения на 15 градусов
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 15, 1)
dst = cv2.warpAffine(img1, M, (cols, rows))

cv2.imshow('Rotated and clipped image', dst)
cv2.waitKey(0)

# Обратный поворот на 15 градусов
M1 = cv2.getRotationMatrix2D((cols / 2, rows / 2), -15, 1)
dst1 = cv2.warpAffine(dst, M1, (cols, rows))

cv2.imshow('Turned back and clipped image', dst1)
cv2.waitKey(0)

# Вычисление разности между исходным и преобразованным изображением
r = cv2.subtract(img1, dst1)
r1 = np.abs(r)

cv2.imshow('Difference', r1)
cv2.waitKey(0)

# Усиленная разность (умноженная на 10)
cv2.imshow('Difference multiplied by 10', 10 * r1)
cv2.waitKey(0)

cv2.destroyAllWindows()
