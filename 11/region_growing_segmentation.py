"""
Сегментация методом регионарного роста (Region Growing)
Демонстрирует алгоритм выделения областей на основе схожести пикселей
с начальной точкой (seed point)
"""
import cv2
import numpy as np

_img = cv2.imread('img/Figures2.png')

# Предварительная фильтрация для уменьшения шума
img = cv2.bilateralFilter(_img, 15, 75, 75)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", img)
cv2.waitKey(1)


def RegionGrowing(img, seedpix, thresh):
    """
    Алгоритм регионарного роста
    Args:
        img: входное изображение
        seedpix: начальная точка [x, y]
        thresh: порог схожести пикселей
    Returns:
        mask: бинарная маска выделенной области
    """
    h, w, __ = img.shape
    img = img.astype('float32')

    x, y = seedpix[0], seedpix[1]

    # Инициализация маски
    mask = np.ones((h, w), np.uint8)
    mask[1:h - 1, 1:w - 1] = 0

    # Инициализация стека для обработки пикселей
    stack = []
    stack.append([x, y])
    mask[y, x] = 1

    # Массив направлений (4-связность)
    directions = [
        [0, -1],   # верх
        [0, 1],    # низ
        [-1, 0],   # лево
        [1, 0]     # право
    ]

    # Алгоритм регионарного роста
    b = 0
    e = 1
    N = 1

    while b < e:
        xx = stack[b][0]
        yy = stack[b][1]
        b += 1

        current_pixel = img[yy, xx, :]

        # Проверка всех соседних пикселей
        for dx, dy in directions:
            nx, ny = xx + dx, yy + dy

            if (mask[ny, nx] == 0 and
                    cv2.norm(current_pixel - img[ny, nx, :]) <= thresh):
                stack.append([nx, ny])
                mask[ny, nx] = 1
                e += 1
                N += 1

    return mask


# Задание начальной точки и запуск алгоритма
seedpix = [142, 78]
mask = RegionGrowing(img, seedpix, 10)

print(f"Mask shape: {mask.shape}")

cv2.namedWindow("ClusteredPPcenters", cv2.WINDOW_NORMAL)
cv2.imshow("ClusteredPPcenters", 255 * mask)
cv2.waitKey(0)

cv2.destroyAllWindows()
