"""
Сравнение алгоритмов сжатия изображений
Демонстрирует различия между PNG и JPEG сжатием
и визуализирует артефакты сжатия
"""
import cv2
import numpy as np
import os

if not os.path.exists('temp'):
    os.makedirs('temp')

img = cv2.imread("img/flowers1.png")

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", img)
cv2.waitKey(0)

# Сжатие в PNG с максимальным сжатием
cv2.imwrite('temp/flowers1_png.png', img,
            [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
flowers1_png = cv2.imread("temp/flowers1_png.png")

cv2.namedWindow("Compressed_png", cv2.WINDOW_NORMAL)
cv2.imshow("Compressed_png", flowers1_png)
cv2.waitKey(0)

# Сжатие в JPEG с заданным качеством
# Значение от 0 до 100 (выше - лучше качество, но больше размер)
jpeg_quality = 80

cv2.imwrite('temp/flowers1_png.jpg', img,
            [cv2.IMWRITE_JPEG_QUALITY, jpeg_quality])
flowers1_jpg = cv2.imread("temp/flowers1_png.jpg")

cv2.namedWindow("Compressed_jpg", cv2.WINDOW_NORMAL)
cv2.imshow("Compressed_jpg", flowers1_jpg)
cv2.waitKey(0)

# Вычисление разности между оригиналом и сжатыми изображениями
Dif_png = abs(img - flowers1_png)
Dif_jpg = abs(img - flowers1_jpg)

cv2.namedWindow("Difference_png", cv2.WINDOW_NORMAL)
cv2.imshow("Difference_png", Dif_png)
cv2.waitKey(0)

cv2.namedWindow("Difference_jpg", cv2.WINDOW_NORMAL)
cv2.imshow("Difference_jpg", Dif_jpg)
cv2.waitKey(0)

cv2.destroyAllWindows()
