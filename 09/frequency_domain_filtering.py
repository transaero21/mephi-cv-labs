"""
Фильтрация в частотной области с режекторным фильтром
Демонстрирует удаление периодического шума с помощью
гауссова режекторного фильтра в частотной области
"""
import cv2
import numpy as np

img = cv2.imread('img/Birds.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Gray", cv2.WINDOW_GUI_NORMAL)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

row, col = gray.shape

# Добавление вертикальных линий для создания периодического шума
for x in range(0, col, 5):
    for y in range(row):
        gray[y, x] = 0

# Добавление гауссовского шума
среднее = 0
дисперсия = 1000
параметр = дисперсия**0.5

gauss = np.random.normal(среднее, параметр, (row, col))
gauss = gauss.reshape(row, col)
noisy_im = abs(np.double(gray) + gauss)

cv2.namedWindow("Noisy", cv2.WINDOW_GUI_NORMAL)
cv2.imshow("Noisy", np.uint8(np.clip(noisy_im, 0, 255)))
cv2.waitKey(0)

# Преобразование Фурье
fft_src = np.fft.fft2(gray)
cntr_src = np.fft.fftshift(fft_src)

# Создание гауссова режекторного фильтра
gauss_reject_filter = np.zeros_like(cntr_src)

freq = 225
b = 145
center = (row / 2., col / 2.)
k = 20

for y in range(row):
    for x in range(col):
        dist1 = np.sqrt(np.power((x - center[1]) - freq, 2))
        dist2 = np.sqrt(np.power((x - center[1] + freq), 2))
        gauss_reject_filter[y, x] = (
            1 / (1 + pow(b / dist1, 2 * k))) * (1 / (1 + pow(b / dist2, 2 * k)))

# Применение фильтра и обратное преобразование
filtered_cntr_src = np.multiply(cntr_src, gauss_reject_filter)
result = np.fft.ifft2(filtered_cntr_src)
resultre = cv2.min(255, abs(result.real))

cv2.namedWindow("Res", cv2.WINDOW_GUI_NORMAL)
cv2.imshow("Res", np.uint8(resultre))
cv2.waitKey(0)

cv2.destroyAllWindows()
