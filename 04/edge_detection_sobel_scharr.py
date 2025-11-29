"""
Детекция граней операторами Собеля и Щарра
Демонстрирует вычисление градиентов по осям X и Y
и различные методы комбинирования результатов
"""
import cv2
import numpy as np

image = cv2.imread('img/Birds.jpg')
cv2.imshow('original', image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Оператор Собеля
Gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0)
Gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1)

# Визуализация градиентов по осям
Gx_image = np.uint8(abs(Gx))
Gx = np.clip(Gx, -255, 255)
Gy = np.clip(Gy, -255, 255)

cv2.namedWindow('Gx', cv2.WINDOW_NORMAL)
cv2.imshow('Gx', Gx_image)
cv2.waitKey(0)

Gy_image = np.uint8(abs(Gy))
cv2.namedWindow('Gy', cv2.WINDOW_NORMAL)
cv2.imshow('Gy', Gy_image)
cv2.waitKey(0)

# Комбинирование градиентов
G = abs(Gx) + abs(Gy)
G = cv2.min(255, G)
G_img = np.uint8(G)

cv2.namedWindow('Sobel', cv2.WINDOW_NORMAL)
cv2.imshow('Sobel', G_img)
cv2.waitKey(0)

# Оператор Щарра (более чувствительный к граням)
Gx = cv2.Scharr(gray, cv2.CV_32F, 1, 0)
Gy = cv2.Scharr(gray, cv2.CV_32F, 0, 1)

G = abs(Gx) + abs(Gy)
G = cv2.min(255, G)
G_img = np.uint8(G)

cv2.namedWindow('Scharr', cv2.WINDOW_NORMAL)
cv2.imshow('Scharr', G_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
