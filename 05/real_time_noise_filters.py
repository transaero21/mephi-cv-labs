"""
Сравнение фильтров в реальном времени на зашумленном видео
Демонстрирует билатеральную и гауссову фильтрацию
для видео с добавленным шумом
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Проверка открытия веб-камеры
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()

    row, col, ch = frame.shape

    # Генерация и добавление шума к кадру
    gauss = np.random.normal(0, 15.0, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)

    noisy = frame + gauss
    noisy = cv2.max(0, noisy)
    noisy1 = np.array(noisy, dtype='uint8')

    # Применение различных фильтров
    framefilered1 = cv2.bilateralFilter(
        noisy1, 10, 55., 55.)  # Билатеральный фильтр
    framefilered2 = cv2.GaussianBlur(noisy1, (11, 11), 4)     # Гауссов фильтр

    cv2.namedWindow('Input', cv2.WINDOW_NORMAL)
    cv2.imshow('Input', noisy1)

    cv2.namedWindow('Bilateral', cv2.WINDOW_NORMAL)
    cv2.imshow('Bilateral', framefilered1)

    cv2.namedWindow('Gaussian', cv2.WINDOW_NORMAL)
    cv2.imshow('Gaussian', framefilered2)

    c = cv2.waitKey(1)
    if c == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
