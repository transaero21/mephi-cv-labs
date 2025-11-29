"""
Детекция граней на видео с веб-камеры с использованием Canny
Демонстрирует обработку видеопотока в реальном времени
и выделение контуров с помощью детектора Канни
"""
import cv2

cap = cv2.VideoCapture(0)

# Проверка открытия веб-камеры
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5,
                       interpolation=cv2.INTER_AREA)

    # Детекция граней с помощью оператора Канни
    frame1 = cv2.Canny(frame, 100, 200)

    cv2.namedWindow('Countors', cv2.WINDOW_NORMAL)
    cv2.imshow('Countors', frame1)

    c = cv2.waitKey(1)
    if c == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
