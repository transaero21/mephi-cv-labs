"""
Повышение контраста с использованием CLAHE
Демонстрирует адаптивное эквалирование гистограммы
в цветовом пространстве LAB для улучшения контраста
"""
import cv2

image = cv2.imread('img/Birds.jpg')
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.imshow('Original', image)

# CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8, 8))

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)  # преобразование из BGR в LAB
l, a, b = cv2.split(lab)  # разделение на 3 канала

l2 = clahe.apply(l)  # применение CLAHE к L-каналу (яркость)

lab = cv2.merge((l2, a, b))  # объединение каналов
image2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # преобразование обратно в BGR

cv2.namedWindow('Increased contrast', cv2.WINDOW_KEEPRATIO)
cv2.imshow('Increased contrast', image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
