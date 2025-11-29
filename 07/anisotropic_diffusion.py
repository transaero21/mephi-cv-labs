"""
Анизотропная диффузия для подавления шума
Демонстрирует метод Пероны-Малика для нелинейной фильтрации
со сохранением границ при удалении шума
"""
import numpy as np
import warnings
import cv2


def anisodiff(
        img,
        niter=1,
        kappa=50,
        gamma=0.1,
        step=(
            1.,
            1.),
    option=1,
        ploton=False):
    """
    Anisotropic diffusion по методу Пероны-Малика

    Arguments:
        img    - входное изображение
        niter  - количество итераций
        kappa  - коэффициент проводимости (20-100)
        gamma  - максимальное значение 0.25 для стабильности
        step   - расстояние между соседними пикселями
        option - 1: уравнение №1 (предпочтение высококонтрастных границ)
                 2: уравнение №2 (предпочтение широких областей)
        ploton - отображать процесс на каждой итерации
    """
    if img.ndim == 3:
        warnings.warn("Only grayscale images allowed, converting to 2D matrix")
        img = img.mean(2)

    img = img.astype('float32')
    imgout = img.copy()

    deltaS = np.zeros_like(imgout)
    deltaE = deltaS.copy()
    NS = deltaS.copy()
    EW = deltaS.copy()
    gS = np.ones_like(imgout)
    gE = gS.copy()

    for ii in range(niter):
        # вычисление разностей
        deltaS[:-1, :] = np.diff(imgout, axis=0)
        deltaE[:, :-1] = np.diff(imgout, axis=1)

        # вычисление градиентов проводимости
        if option == 1:
            gS = np.exp(-(deltaS / kappa)**2.) / step[0]
            gE = np.exp(-(deltaE / kappa)**2.) / step[1]
        elif option == 2:
            gS = 1. / (1. + (deltaS / kappa)**2.) / step[0]
            gE = 1. / (1. + (deltaE / kappa)**2.) / step[1]

        # обновление матриц
        E = gE * deltaE
        S = gS * deltaS

        NS[:] = S
        EW[:] = E
        NS[1:, :] -= S[:-1, :]
        EW[:, 1:] -= E[:, :-1]

        # обновление изображения
        imgout += gamma * (NS + EW)

    return imgout


# Основная программа
img = cv2.imread('img/Birds.jpg', 0)

cv2.namedWindow("Original", cv2.WINDOW_GUI_NORMAL)
cv2.imshow("Original", img)
cv2.waitKey(0)

row, col = img.shape

# Добавление гауссовского шума
среднее = 0
дисперсия = 1600
параметр = дисперсия**0.5

gauss = np.random.normal(среднее, параметр, (row, col))
noisy = img.astype('float32') + gauss
noisy_im = np.clip(noisy, 0, 255)

cv2.namedWindow("Noisy", cv2.WINDOW_GUI_NORMAL)
cv2.imshow("Noisy", np.uint8(noisy_im))
cv2.waitKey(0)

# Применение анизотропной диффузии
Res = anisodiff(
    noisy_im,
    niter=20,
    kappa=50,
    gamma=0.1,
    step=(
        1.,
        1.),
    option=1,
    ploton=False)

cv2.namedWindow("Result", cv2.WINDOW_GUI_NORMAL)
cv2.imshow("Result", Res.astype('uint8'))
cv2.waitKey(0)
cv2.destroyAllWindows()
