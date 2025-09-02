import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from laba_logging import *
InitLogFile()
InitFile(__file__)


import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Создание графика
plt.figure(figsize=(10, 6))  # Размер графика
plt.plot(x, y, marker='o', linestyle='-', color='blue', linewidth=2, markersize=8)

# Настройки графика
plt.title('Пример линейного графика', fontsize=16)
plt.xlabel('Ось X', fontsize=12)
plt.ylabel('Ось Y', fontsize=12)
plt.grid(True, alpha=0.3)

# Показать график
plt.show()