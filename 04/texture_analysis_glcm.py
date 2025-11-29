"""
Текстурный анализ с помощью матрицы совпадений градаций серого (GLCM)
Демонстрирует вычисление текстурных характеристик:
контраст, диссимилярность, однородность, энергия, корреляция, ASM
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import io, feature, exposure

# Загрузка изображения в градациях серого
image = cv2.imread('img/wood.jpg', cv2.IMREAD_GRAYSCALE)

# Отображение исходного изображения
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.show()

# Вычисление матрицы совпадений градаций серого (GLCM)
# distances=[1] - расстояние между пикселями 1
# angles=[0] - угол 0 градусов (горизонтальное направление)
# levels=256 - количество уровней яркости
# symmetric=True - симметричная матрица
# normed=True - нормализованная матрица
glcm = feature.graycomatrix(image, distances=[1], angles=[0], levels=256,
                            symmetric=True, normed=True)

# Извлечение текстурных характеристик
contrast = feature.graycoprops(glcm, 'contrast')
dissimilarity = feature.graycoprops(glcm, 'dissimilarity')
homogeneity = feature.graycoprops(glcm, 'homogeneity')
energy = feature.graycoprops(glcm, 'energy')
correlation = feature.graycoprops(glcm, 'correlation')
ASM = feature.graycoprops(glcm, 'ASM')

# Вывод вычисленных характеристик
print(f'Contrast: {contrast[0][0]}')
print(f'Dissimilarity: {dissimilarity[0][0]}')
print(f'Homogeneity: {homogeneity[0][0]}')
print(f'Energy: {energy[0][0]}')
print(f'Correlation: {correlation[0][0]}')
print(f'ASM: {ASM[0][0]}')

# Дополнительная информация о характеристиках:
# Контраст - мера локальных вариаций в изображении
# Диссимилярность - мера различий между соседними пикселями
# Однородность - мера близости распределения GLCM к диагонали
# Энергия - мера упорядоченности текстуры
# Корреляция - мера линейной зависимости серых уровней
# ASM (Angular Second Moment) - мера однородности текстуры
