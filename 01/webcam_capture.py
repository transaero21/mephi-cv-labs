"""
Захват видео с веб-камеры
Демонстрирует работу с видеопотоком:
- инициализация камеры, чтение кадров, отображение, выход по ESC
"""
import cv2

cap = cv2.VideoCapture(0)

while True:
    __, frame = cap.read()
    cv2.imshow('Input', frame)
    c = cv2.waitKey(1)
    if c == 27:  # Клавиша ESC
        break

cv2.destroyAllWindows()
