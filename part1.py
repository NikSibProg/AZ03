import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0
std_dev = 1
num_samples = 1000

# Генерация случайных данных
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.hist(data, bins=30, color='blue', alpha=0.7, edgecolor='black')
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
