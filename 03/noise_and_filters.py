"""
Добавление шума и применение фильтров
Демонстрирует:
- добавление гауссовского шума к изображению
- сглаживание с помощью гауссова и боксового фильтров
"""
import cv2
import numpy as np

image = cv2.imread('img/Birds.jpg')
cv2.imshow('original', image)

row, col, ch = image.shape

# Генерация гауссовского шума
gauss = np.random.normal(0, 15.0, (row, col, ch))
gauss = gauss.reshape(row, col, ch)

# Добавление шума к изображению
noisy = gauss + image.astype(np.float32)
img_noisy = noisy.clip(0, 255)

cv2.namedWindow('Noisy', cv2.WINDOW_NORMAL)
cv2.imshow('Noisy', img_noisy.astype(np.uint8))

# Применение гауссова фильтра
img_flt_gaus = cv2.GaussianBlur(img_noisy, (5, 5), 2)
cv2.namedWindow('Filtr_Gaus', cv2.WINDOW_NORMAL)
cv2.imshow('Filtr_Gaus', img_flt_gaus.astype(np.uint8))

# Применение боксового фильтра
img_flt_box = cv2.boxFilter(img_noisy, -1, (5, 5))
cv2.namedWindow('Filtr_Box', cv2.WINDOW_NORMAL)
cv2.imshow('Filtr_Box', img_flt_box.astype(np.uint8))

cv2.waitKey(0)
cv2.destroyAllWindows()
