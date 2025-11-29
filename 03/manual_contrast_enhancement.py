"""
Ручное повышение контраста с использованием фильтра
Демонстрирует применение пользовательского ядра свертки
для ручного повышения резкости и контраста изображения
"""
import cv2
import numpy as np

image = cv2.imread('img/Birds.jpg')
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.imshow('Original', image)
cv2.waitKey(0)

rows, cols, ch = image.shape
image1 = cv2.copyTo(image, None)

# Создание ядра фильтра для повышения резкости
f = np.zeros((3, 3))
f[0, 1] = -1
f[1, 0] = -1
f[1, 1] = 5
f[1, 2] = -1
f[2, 1] = -1

# Применение фильтра к каждому каналу вручную
for y in range(1, rows - 1):
    for x in range(1, cols - 1):
        image1[y,
               x,
               0] = min(255,
                        abs(image[y,
                                  x,
                                  0] * f[0,
                                         1] + image[y,
                                                    x - 1,
                                                    0] * f[1,
                                                           0] + image[y,
                                                                      x,
                                                                      0] * f[1,
                                                                             1] + image[y,
                                                                                        x + 1,
                                                                                        0] * f[1,
                                                                                               2] + image[y + 1,
                                                                                                          x,
                                                                                                          0] * f[2,
                                                                                                                 1]))
        image1[y,
               x,
               1] = min(255,
                        abs(image[y - 1,
                                  x,
                                  1] * f[0,
                                         1] + image[y,
                                                    x - 1,
                                                    1] * f[1,
                                                           0] + image[y,
                                                                      x,
                                                                      1] * f[1,
                                                                             1] + image[y,
                                                                                        x + 1,
                                                                                        1] * f[1,
                                                                                               2] + image[y + 1,
                                                                                                          x,
                                                                                                          1] * f[2,
                                                                                                                 1]))
        image1[y,
               x,
               2] = min(255,
                        abs(image[y - 1,
                                  x,
                                  2] * f[0,
                                         1] + image[y,
                                                    x - 1,
                                                    2] * f[1,
                                                           0] + image[y,
                                                                      x,
                                                                      2] * f[1,
                                                                             1] + image[y,
                                                                                        x + 1,
                                                                                        2] * f[1,
                                                                                               2] + image[y + 1,
                                                                                                          x,
                                                                                                          2] * f[2,
                                                                                                                 1]))

cv2.namedWindow('Processed', cv2.WINDOW_NORMAL)
cv2.imshow('Processed', image1)
cv2.waitKey(0)
