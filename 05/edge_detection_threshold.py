"""
Детекция граней с пороговой обработкой
Демонстрирует применение операторов Собеля и Щарра
с дополнительной пороговой обработкой для выделения граней
"""
import cv2
import numpy as np

img = cv2.imread('img/Birds.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', img)
cv2.waitKey(0)

# Оператор Собеля с порогом
Gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0)
Gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1)

G = abs(Gx) + abs(Gy)
G = 255 * (abs(Gx) + abs(Gy) > 255)  # Пороговая обработка
G = cv2.min(255, G)
G = np.uint8(G)

cv2.namedWindow('Sobel', cv2.WINDOW_NORMAL)
cv2.imshow('Sobel', G)
cv2.waitKey(0)

# Оператор Щарра с порогом
Gx = cv2.Scharr(gray, cv2.CV_32F, 1, 0)
Gy = cv2.Scharr(gray, cv2.CV_32F, 0, 1)

G = abs(Gx) + abs(Gy)
G = 255 * (abs(Gx) + abs(Gy) > 355)  # Пороговая обработка
G = cv2.min(255, G)
G = np.uint8(G)

cv2.namedWindow('Scharr', cv2.WINDOW_NORMAL)
cv2.imshow('Scharr', G)
cv2.waitKey(0)

cv2.destroyAllWindows()
