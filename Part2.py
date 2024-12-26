import numpy as np  # Импортируем библиотеку numpy
import matplotlib.pyplot as plt

# Генерация случайных данных
x = np.random.rand(100)
y = np.random.rand(100)

# Построение диаграммы рассеяния
plt.scatter(x, y, color='green', alpha=0.6, edgecolor='black')
plt.title('Диаграмма рассеяния')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()