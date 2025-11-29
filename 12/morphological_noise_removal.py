"""
Удаление шума с помощью морфологических операций
Демонстрирует использование дилатации и эрозии
для удаления шума типа "соль и перец"
"""
import cv2
import numpy as np

I = cv2.imread('img/Jorig.jpg')

# Бинаризация изображения
__, I = cv2.threshold(I, 70, 255, cv2.THRESH_BINARY)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", I)
cv2.waitKey(0)

Inoise = cv2.imread('img/JwithPepper.jpg')

cv2.namedWindow("JwithNoise", cv2.WINDOW_NORMAL)
cv2.imshow("JwithNoise", Inoise)
cv2.waitKey(0)

# Морфологическая обработка: дилатация для удаления черного шума
kernel = np.ones((3, 3), np.uint8)
R = cv2.dilate(Inoise, kernel)

cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
cv2.imshow("Result", R)
cv2.waitKey(0)

# Эрозия для восстановления размера объектов
kernel1 = np.ones((4, 4), np.uint8)
RR = cv2.erode(R, kernel1)

cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
cv2.imshow("Result", RR)
cv2.waitKey(0)

cv2.destroyAllWindows()
