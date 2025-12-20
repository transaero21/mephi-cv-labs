"""
Обнаружение объектов с помощью YOLO на изображении
Демонстрирует использование модели YOLO от Ultralytics
для обнаружения объектов на статическом изображении
с автоматическим определением доступного устройства
"""
import cv2
import numpy as np
from ultralytics import YOLO
import torch

def get_device():
    """Определение доступного устройства для вычислений"""
    if torch.cuda.is_available():
        return torch.device('cuda')
    elif torch.backends.mps.is_available():
        return torch.device('mps')
    else:
        return torch.device('cpu')

# Выбор устройства (GPU/MPS/CPU)
mydevice = get_device()
print(f"Используемое устройство: {mydevice}")

# Загрузка модели YOLO (nano версия для скорости)
model = YOLO('yolo12n.pt')

# Детекция объектов на изображении
results = model.predict('img/Birds.jpg', device=mydevice)

# Визуализация результатов
result = results[0].plot()

cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
cv2.imshow("Result", result)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Дополнительная информация о результатах
print(f"Обнаружено объектов: {len(results[0].boxes)}")
if len(results[0].boxes) > 0:
    print("Классы обнаруженных объектов:")
    for i, box in enumerate(results[0].boxes):
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        print(f"  {i+1}: Класс {cls}, уверенность {conf:.2f}")