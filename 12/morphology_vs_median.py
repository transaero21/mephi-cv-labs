"""
Сравнение морфологической фильтрации и медианного фильтра
Демонстрирует различные подходы к удалению шума
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

# Морфологическая фильтрация (открытие)
kernel = np.ones((3, 3), np.uint8)
R = cv2.dilate(Inoise, kernel)

kernel1 = np.ones((5, 5), np.uint8)
RR = cv2.erode(R, kernel1)

cv2.namedWindow("ResultMorpho", cv2.WINDOW_NORMAL)
cv2.imshow("ResultMorpho", RR)
cv2.waitKey(0)

# Медианная фильтрация
RR1 = cv2.medianBlur(Inoise, 5)
cv2.namedWindow("ResultMedian", cv2.WINDOW_NORMAL)
cv2.imshow("ResultMedian", RR1)
cv2.waitKey(0)

cv2.destroyAllWindows()
