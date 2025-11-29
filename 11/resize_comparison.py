"""
Сравнение алгоритмов изменения размера изображения
Демонстрирует различные методы интерполяции при масштабировании
"""
import cv2
import numpy as np

img = cv2.imread('img/Birds.jpg')

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", img)
cv2.waitKey(0)

a = 0.7  # Коэффициент масштабирования

new_height = int(a * img.shape[0])
new_width = int(a * img.shape[1])

# Изменение размера с различными методами интерполяции
# Синтаксис: cv2.resize(src, dsize, dst=None, fx=None, fy=None, interpolation)

resized_nearest = cv2.resize(
    img, (0, 0), fx=a, fy=a, interpolation=cv2.INTER_NEAREST)
resized_linear = cv2.resize(img, (0, 0), fx=a, fy=a,
                            interpolation=cv2.INTER_LINEAR)
resized_cubic = cv2.resize(img, (0, 0), fx=a, fy=a,
                           interpolation=cv2.INTER_CUBIC)
resized_lanczos = cv2.resize(
    img, (0, 0), fx=a, fy=a, interpolation=cv2.INTER_LANCZOS4)

# Отображение результатов
cv2.namedWindow("Resized1", cv2.WINDOW_NORMAL)
cv2.imshow("Resized1", resized_nearest)
cv2.waitKey(0)

cv2.namedWindow("Resized2", cv2.WINDOW_NORMAL)
cv2.imshow("Resized2", resized_linear)
cv2.waitKey(0)

cv2.namedWindow("Resized3", cv2.WINDOW_NORMAL)
cv2.imshow("Resized3", resized_cubic)
cv2.waitKey(0)

cv2.namedWindow("Resized4", cv2.WINDOW_NORMAL)
cv2.imshow("Resized4", resized_lanczos)
cv2.waitKey(0)

cv2.destroyAllWindows()
