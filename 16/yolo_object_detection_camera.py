"""
Обнаружение объектов с помощью YOLO на видео в реальном времени
Демонстрирует использование YOLO для детекции объектов
с веб-камеры с поддержкой GPU/MPS/CPU
"""
import cv2
import numpy as np
from ultralytics import YOLO
import torch


def get_device():
    """Определение доступного устройства для вычислений"""
    if torch.cuda.is_available():
        return torch.device('cuda')
    elif torch.backends.mps.is_available():  # Для Apple Silicon
        return torch.device('mps')
    else:
        return torch.device('cpu')


model = YOLO('yolo12x.pt')
device = get_device()
print(f"Используемое устройство: {device}")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Ошибка: не удалось открыть веб-камеру")
    exit()

print("Нажмите 'q' для выхода...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Ошибка: не удалось получить кадр")
        break

    # Детекция объектов на кадре
    results = model.predict(frame, device=device, verbose=False)

    # Визуализация результатов
    result_frame = results[0].plot()

    # Отображение FPS (опционально)
    cv2.putText(result_frame, f"Device: {str(device).upper()}",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
    cv2.imshow("Result", result_frame)

    # Выход по нажатию 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Выход...")
