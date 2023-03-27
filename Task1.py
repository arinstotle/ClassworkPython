import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi)
# учитываем периодичность графика
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

plt.figure(figsize=(6, 6))
plt.plot(x, y, color='red')
plt.fill(x, y, color='red', alpha=0.5)
plt.xlabel('t')
plt.ylabel('x')
plt.show()