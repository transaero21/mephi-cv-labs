"""
Визуализация сравнения методов интерполяции
Демонстрирует различия между методами в едином представлении
с использованием matplotlib
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Загрузка и изменение размера изображения разными методами
img = cv2.imread('img/Birds.jpg')
a = 0.7

resized_nearest = cv2.resize(
    img, (0, 0), fx=a, fy=a, interpolation=cv2.INTER_NEAREST)
resized_linear = cv2.resize(img, (0, 0), fx=a, fy=a,
                            interpolation=cv2.INTER_LINEAR)
resized_cubic = cv2.resize(img, (0, 0), fx=a, fy=a,
                           interpolation=cv2.INTER_CUBIC)
resized_lanczos = cv2.resize(
    img, (0, 0), fx=a, fy=a, interpolation=cv2.INTER_LANCZOS4)

# Конвертация BGR в RGB для корректного отображения в matplotlib
resized_nearest_rgb = cv2.cvtColor(resized_nearest, cv2.COLOR_BGR2RGB)
resized_linear_rgb = cv2.cvtColor(resized_linear, cv2.COLOR_BGR2RGB)
resized_cubic_rgb = cv2.cvtColor(resized_cubic, cv2.COLOR_BGR2RGB)
resized_lanczos_rgb = cv2.cvtColor(resized_lanczos, cv2.COLOR_BGR2RGB)

# Создание фигуры с несколькими subplots
fig = plt.figure(figsize=(10, 7))

# Первое изображение - Nearest Neighbor
plt.subplot(2, 2, 1)  # 2 строки, 2 столбца, первая позиция
plt.imshow(resized_nearest_rgb)
plt.axis('off')  # Скрыть оси
plt.title("INTER_NEAREST")

# Второе изображение - Linear
plt.subplot(2, 2, 2)  # 2 строки, 2 столбца, вторая позиция
plt.imshow(resized_linear_rgb)
plt.axis('off')
plt.title("INTER_LINEAR")

# Третье изображение - Cubic
plt.subplot(2, 2, 3)  # 2 строки, 2 столбца, третья позиция
plt.imshow(resized_cubic_rgb)
plt.axis('off')
plt.title("INTER_CUBIC")

# Четвертое изображение - Lanczos
plt.subplot(2, 2, 4)  # 2 строки, 2 столбца, четвертая позиция
plt.imshow(resized_lanczos_rgb)
plt.axis('off')
plt.title("INTER_LANCZOS4")

plt.tight_layout()
plt.show()
