"""
Продвинутые методы фильтрации изображений
Демонстрирует адаптивный манифолдный фильтр и анизотропную диффузию
из модуля ximgproc OpenCV
"""
import cv2
import numpy as np

I = cv2.imread('img/Birds.jpg')

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", I)
cv2.waitKey(0)

row, col, ch = I.shape

# Добавление шума
gauss = np.random.normal(0, 25.0, (row, col, ch))
II = I.astype('float')
noisy = II + gauss
noisy = np.clip(noisy, 0, 255)
noisy = noisy.astype('uint8')

cv2.namedWindow("Noisy", cv2.WINDOW_NORMAL)
cv2.imshow("Noisy", noisy)
cv2.waitKey(0)

# Применение адаптивного манифолдного фильтра
J = cv2.ximgproc.amFilter(noisy, noisy, 3.9, 0.2)

cv2.namedWindow("Result_AdaptiveManifoldFilter", cv2.WINDOW_NORMAL)
cv2.imshow("Result_AdaptiveManifoldFilter", J.astype('uint8'))
cv2.waitKey(0)

# Применение анизотропной диффузии
J1 = cv2.ximgproc.anisotropicDiffusion(noisy, 0.07, 0.075, 2000)
anisotrop_median = cv2.medianBlur(J1, 3)

cv2.namedWindow("Result_anisotrop_&_median", cv2.WINDOW_NORMAL)
cv2.imshow("Result_anisotrop_&_median", anisotrop_median)
cv2.waitKey(0)

cv2.destroyAllWindows()
