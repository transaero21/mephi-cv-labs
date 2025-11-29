"""
Сравнение методов бинаризации
Демонстрирует глобальную пороговую обработку,
метод Оцу и комбинацию с гауссовым сглаживанием
"""
import cv2
import numpy as np

img = cv2.imread('img/Birds.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", gray)
cv2.waitKey(0)

# Глобальная пороговая обработка
ret1, th1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Метод Оцу (автоматический выбор порога)
ret2, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Метод Оцу после гауссова сглаживания
blur = cv2.GaussianBlur(gray, (5, 5), 0)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Отображение результатов (инвертированные для лучшей видимости)
cv2.namedWindow("Binary", cv2.WINDOW_NORMAL)
cv2.imshow("Binary", 255 - th1)
cv2.waitKey(0)

cv2.namedWindow("OTSU", cv2.WINDOW_NORMAL)
cv2.imshow("OTSU", 255 - th2)
cv2.waitKey(0)

cv2.namedWindow("OTSUandCAUSS", cv2.WINDOW_NORMAL)
cv2.imshow("OTSUandCAUSS", 255 - th3)
cv2.waitKey(0)

cv2.destroyAllWindows()
