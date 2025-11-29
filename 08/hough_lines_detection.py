"""
Детекция линий с помощью преобразования Хафа
Демонстрирует обнаружение прямых линий на изображении
с использованием детектора Канни и преобразования Хафа
"""
import cv2
import numpy as np
import math

img = cv2.imread("img/Figures1.png")
img = 255 - img  # инверсия цветов

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.imshow('Original', img)
cv2.waitKey(0)

# Детекция граней с помощью оператора Канни
dst = cv2.Canny(img, 50, 200, None, 3)

cv2.namedWindow('Canny', cv2.WINDOW_NORMAL)
cv2.imshow('Canny', dst)
cv2.waitKey(0)

# Обнаружение линий с помощью преобразования Хафа
lines = cv2.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)

result = np.zeros(np.shape(img), "uint8")

# Отрисовка обнаруженных линий
if lines is not None:
    for i in range(0, len(lines)):
        r = lines[i][0][0]      # расстояние от начала координат
        theta = lines[i][0][1]  # угол в радианах
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * r
        y0 = b * r

        # Вычисление точек для отрисовки линии
        pt1 = (int(x0 + 2000 * (-b)), int(y0 + 2000 * (a)))
        pt2 = (int(x0 - 2000 * (-b)), int(y0 - 2000 * (a)))
        cv2.line(result, pt1, pt2, (150, 0, 150), 1, cv2.LINE_AA)

# Отображение результата с наложением на исходное изображение
cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
cv2.imshow('Result', cv2.min((255, 255, 255), result + img))
cv2.waitKey(0)

cv2.destroyAllWindows()
