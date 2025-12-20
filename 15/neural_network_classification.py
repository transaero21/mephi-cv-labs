"""
Нейронная сеть для классификации с использованием PyTorch
Демонстрирует создание и обучение нейронной сети
для бинарной классификации кольцеобразных данных
"""
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np

# Параметры данных и обучения
DataSize = 1000
epochs = 2000  # число эпох
scale = 100
radius = scale / 4
center = scale / 2.

# Генерация случайных точек
X = scale * torch.rand(DataSize, 2)

# Создание целевых меток (кольцеобразная область)
YY = np.zeros(shape=(DataSize, 1), dtype='float32')

for j in range(0, DataSize):
    # fmt: off
    if (X[j, 0] - scale*0.5)*(X[j, 0] - scale*0.5) + \
       (X[j, 1] - scale*0.5)*(X[j, 1] - scale*0.5) <= scale*scale*0.25*0.25 and \
       (X[j, 0] - scale*0.5)*(X[j, 0] - scale*0.5) + \
       (X[j, 1] - scale*0.5)*(X[j, 1] - scale*0.5) >= scale*scale*0.1*0.1:
    # fmt: on
        YY[j] = 1

Y = torch.from_numpy(YY)

# Визуализация данных
plt.figure(figsize=(5, 5))
plt.scatter(X.numpy()[:, 0], X.numpy()[:, 1], c=Y.numpy()[:, 0],
            s=30, cmap=plt.cm.Paired, edgecolors='k')
plt.title("Исходные данные (кольцевая область)")
plt.show()

# Архитектура нейронной сети
nX, nH, nY = 2, 5, 1  # входной, скрытый и выходной слои

model = nn.Sequential(
    nn.BatchNorm1d(nX),  # Batch нормализация входных данных
    nn.Linear(nX, nH),   # первый скрытый слой
    nn.BatchNorm1d(nH),  # Batch нормализация
    nn.Sigmoid(),        # активация скрытого слоя
    nn.BatchNorm1d(nH),  # Batch нормализация

    nn.Linear(nH, nH),   # второй скрытый слой
    nn.BatchNorm1d(nH),  # Batch нормализация
    nn.Sigmoid(),        # активация скрытого слоя

    nn.BatchNorm1d(nH),  # Batch нормализация
    nn.Linear(nH, nY),   # выходной слой
    nn.Sigmoid()         # сигмоида для бинарной классификации
)

# Функция потерь и оптимизатор
loss = nn.BCELoss()  # Binary Cross Entropy Loss
optimizer = torch.optim.SGD(model.parameters(), lr=0.5, momentum=0.8)


def fit(model, X, Y, batch_size=100, train=True):
    """Функция обучения/оценки модели"""
    model.train(train)  # важен для Dropout, BatchNorm
    # ошибка, точность, количество батчей
    sumL, sumA, numB = 0, 0, int(len(X) / batch_size)

    for i in range(0, numB * batch_size, batch_size):
        xb = X[i: i + batch_size]  # текущий батч
        yb = Y[i: i + batch_size]

        y = model(xb)  # прямое распространение
        L = loss(y, yb)  # вычисление ошибки

        if train:  # режим обучения
            optimizer.zero_grad()  # обнуляем градиенты
            L.backward()  # вычисляем градиенты
            optimizer.step()  # обновляем параметры

        sumL += L.item()  # суммарная ошибка
        sumA += (y.round() == yb).float().mean()  # точность

    return sumL / numB, sumA / numB


# Оценка модели до обучения
print("До обучения: loss: %.4f accuracy: %.4f" % fit(model, X, Y, train=False))

# Процесс обучения
for epoch in range(epochs):
    # Перемешивание данных для каждой эпохи
    idx = [i for i in range(DataSize)]
    idx_p = np.random.permutation(idx)
    sort = np.argsort(idx_p)

    Xp = X[sort]
    Yp = Y[sort]

    L, A = fit(model, Xp, Yp)  # одна эпоха обучения

    if epoch % 100 == 0 or epoch == epochs - 1:
        print(f'Эпоха: {epoch:5d} loss: {L:.4f} accuracy: {A:.4f}')

# Оценка модели после обучения
Res = model(X)
Res1 = Res.cpu().detach().numpy()

# Подсчет ошибок классификации
N = 0
for j in range(DataSize):
    if Res1[j] >= 0.5:
        N = N + 1 - Y[j]
    else:
        N = N + Y[j]

print(
    f"Ошибок классификации: {int(N.item())} из {DataSize} ({N.item()/DataSize*100:.2f}%)")
