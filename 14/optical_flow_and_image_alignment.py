"""
Оптический поток и выравнивание изображений
Демонстрирует алгоритм Лукаса-Канаде для отслеживания ключевых точек
и аффинное/проективное выравнивание изображений
"""
import cv2
import numpy as np

# Загрузка двух последовательных кадров
I1 = cv2.imread('img/frame0001.jpg')
I2 = cv2.imread('img/frame0020.jpg')

cv2.namedWindow("Image1", cv2.WINDOW_NORMAL)
cv2.imshow("Image1", I1)
cv2.waitKey(0)

cv2.namedWindow("Image2", cv2.WINDOW_NORMAL)
cv2.imshow("Image2", I2)
cv2.waitKey(0)

# Вычисление разности изображений
D0 = abs(cv2.subtract(I1, I2))

cv2.namedWindow("Dif", cv2.WINDOW_NORMAL)
cv2.imshow("Dif", D0)
cv2.waitKey(0)

rows, cols, ch = I1.shape

# Преобразование в градации серого
I1gray = cv2.cvtColor(I1, cv2.COLOR_BGR2GRAY)
I2gray = cv2.cvtColor(I2, cv2.COLOR_BGR2GRAY)

# Обнаружение особенностей для отслеживания (метод хороших особенностей)
p1 = cv2.goodFeaturesToTrack(I1gray, 100, 0.01, 50)

# Параметры для вычисления оптического потока Лукаса-Канаде
lk_params = dict(winSize=(95, 95),
                 maxLevel=3,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))  # noqa: E501

# Вычисление оптического потока
p2, st, err = cv2.calcOpticalFlowPyrLK(I1gray, I2gray, p1, None, **lk_params)

if p1 is not None:
    # Отбор только успешно отслеженных точек
    good_new = p2[st == 1]
    good_old = p1[st == 1]

# Поиск оптимального аффинного преобразования
eps = 1E10  # начальное значение ошибки
k = 0
n = good_old[:, 1].size

# Перебор троек точек для нахождения лучшего аффинного преобразования
for x in range(3, n, 3):
    a = good_old[x - 3:x]  # три точки на первом изображении
    b = good_new[x - 3:x]  # соответствующие точки на втором изображении

    # Вычисление аффинного преобразования
    A = cv2.getAffineTransform(a.astype(np.float32), b.astype(np.float32))

    # Применение преобразования к первому изображению
    I1affine = cv2.warpAffine(I1, A, (cols, rows))

    # Вычисление ошибки совпадения
    s = np.sum(abs(cv2.subtract(I1affine, I2)))

    if s < eps:
        eps = s  # обновление минимальной ошибки
        k = x    # сохранение индекса лучшей тройки

# Применение наилучшего аффинного преобразования
a = good_old[k - 3:k].astype(np.float32)
b = good_new[k - 3:k].astype(np.float32)

A = cv2.getAffineTransform(a, b)
I1_affine = cv2.warpAffine(I1, A, (cols, rows))

cv2.namedWindow("I1_affine", cv2.WINDOW_NORMAL)
cv2.imshow("I1_affine", I1_affine)
cv2.waitKey(0)

# Разность после аффинного выравнивания
DifAff = cv2.subtract(I1_affine, I2)
cv2.namedWindow("DifAff", cv2.WINDOW_NORMAL)
cv2.imshow("DifAff", DifAff)
cv2.waitKey(0)

# Проективное преобразование (гомография) с RANSAC
H, __ = cv2.findHomography(good_old, good_new, cv2.RANSAC, 1000)
I1_perspective = cv2.warpPerspective(I1, H, (cols, rows))

# Разность после проективного выравнивания
DifPersp = abs(cv2.subtract(I1_perspective, I2))
cv2.namedWindow("DifPersp", cv2.WINDOW_NORMAL)
cv2.imshow("DifPersp", DifPersp)
cv2.waitKey(0)

cv2.destroyAllWindows()
