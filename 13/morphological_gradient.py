"""
Морфологический градиент и сравнение с оператором Собеля
Демонстрирует различные методы выделения границ
"""
import cv2
import numpy as np

I = cv2.imread('img/flowers1.png')
I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", I)
cv2.waitKey(0)

# Морфологический градиент
kernel = np.ones((2, 2), np.uint8)
R = cv2.morphologyEx(I_gray, cv2.MORPH_GRADIENT, kernel)

# Бинаризация морфологического градиента
__, RR = cv2.threshold(R, 5, 255, cv2.THRESH_BINARY)

cv2.namedWindow("ResultMorphoGrad", cv2.WINDOW_NORMAL)
cv2.imshow("ResultMorphoGrad", RR)
cv2.waitKey(0)

# Градиент Собеля
RR1x = cv2.Sobel(I_gray, cv2.CV_32F, 1, 0)
RR1y = cv2.Sobel(I_gray, cv2.CV_32F, 0, 1)

RR1 = abs(RR1x) + abs(RR1y)
RR1 = np.clip(RR1, 0, 255)

# Бинаризация градиента Собеля методом Оцу
__, RR2 = cv2.threshold(RR1.astype('uint8'), 0, 255,
                        cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.namedWindow("ResultSobelGrad", cv2.WINDOW_NORMAL)
cv2.imshow("ResultSobelGrad", RR2)
cv2.waitKey(0)

cv2.destroyAllWindows()
