"""
Идеальный низкочастотный фильтр в частотной области
Демонстрирует фильтрацию Фурье с идеальным фильтром
для удаления высокочастотного шума
"""
import cv2
import numpy as np

img = cv2.imread('img/Birds.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

row, col = gray.shape

# Добавление гауссовского шума
среднее = 0
дисперсия = 200
параметр = дисперсия**0.5

gauss = np.random.normal(среднее, параметр, (row, col))
noisy = gray.astype('float32') + gauss
noisy = np.clip(abs(noisy), 0, 255)

cv2.namedWindow("Noisy", cv2.WINDOW_GUI_NORMAL)
cv2.imshow("Noisy", np.uint8(noisy))
cv2.waitKey(0)

# Преобразование Фурье
fft_src = np.fft.fft2(noisy)
cntr_src = np.fft.fftshift(fft_src)

# Создание идеального низкочастотного фильтра
ideal_low_pass_filter = np.zeros_like(cntr_src)
filter_radius = 60
center = (row / 2., col / 2.)

# Построение идеального фильтра
for y in range(row):
    for x in range(col):
        dist_from_center = np.sqrt(
            np.power((y - center[0]), 2) + np.power((x - center[1]), 2))
        if dist_from_center >= filter_radius:
            ideal_low_pass_filter[y, x] = 0
        else:
            ideal_low_pass_filter[y, x] = 1

# Применение фильтра и обратное преобразование
filtered_cntr_src = np.multiply(cntr_src, ideal_low_pass_filter)
result = np.fft.ifft2(filtered_cntr_src)
resultre = cv2.min(255, abs(result.real)).astype('uint8')

cv2.namedWindow("Res", cv2.WINDOW_GUI_NORMAL)
cv2.imshow("Res", resultre)
cv2.waitKey(0)
cv2.destroyAllWindows()
