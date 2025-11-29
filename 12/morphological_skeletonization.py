"""
Морфологический скелетонизация бинарных изображений
Демонстрирует алгоритм построения скелета объекта
с использованием морфологических операций
"""
import cv2
import numpy as np

I = cv2.imread('img/Jorig.jpg')

# Бинаризация изображения
t, I = cv2.threshold(I, 70, 255, cv2.THRESH_BINARY)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", I)
cv2.waitKey(1)


def skeletonize(J):
    """
    Алгоритм скелетонизации с использованием морфологических операций
    """
    J1 = J.copy()
    skel = J.copy()
    n = 0
    skel[:, :] = 0
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    while True:
        eroded = cv2.morphologyEx(J1, cv2.MORPH_ERODE, kernel)
        temp = cv2.morphologyEx(eroded, cv2.MORPH_DILATE, kernel)
        temp = cv2.subtract(J1, temp)
        skel = cv2.bitwise_or(skel, temp)
        J1[:, :] = eroded[:, :]
        n = n + 1
        if np.sum(J1 == 255) == 0:
            break
    print(f'Iterations: {n - 1}')
    return skel


# Применение скелетонизации
Res = skeletonize(I)

cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
cv2.imshow("Result", Res)
cv2.waitKey(1)

# Морфологическое закрытие для улучшения результата
kernel = np.ones((5, 5), np.uint8)
Res2 = cv2.morphologyEx(Res, cv2.MORPH_CLOSE, kernel)

cv2.namedWindow("Result2", cv2.WINDOW_NORMAL)
cv2.imshow("Result2", Res2)
cv2.waitKey(0)

cv2.destroyAllWindows()
