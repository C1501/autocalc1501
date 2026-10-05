import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de x, evitando las asíntotas en x = -1, 0, 1
x1 = np.linspace(-2.5, -1.1, 400)
x2 = np.linspace(-0.9, -0.05, 400)
x3 = np.linspace(0.05, 0.9, 400)
x4 = np.linspace(1.1, 3.0, 400)

# Antiderivada F(x) con C = 0 para las diferentes regiones
def F(x):
    return np.log(np.abs((x - 1)**3 * (x + 1) / (x**3)))

y1 = F(x1)
y2 = F(x2)
y3 = F(x3)
y4 = F(x4)

plt.figure(figsize=(4, 3))
plt.plot(x1, y1, color='b')
plt.plot(x2, y2, color='b')
plt.plot(x3, y3, color='b', label=r'$F(x)$ con $C=0$')
plt.plot(x4, y4, color='b')

plt.axvline(x=0, color='r', linestyle='--', alpha=0.5)
plt.axvline(x=1, color='g', linestyle='--', alpha=0.5)
plt.axvline(x=-1, color='g', linestyle='--', alpha=0.5)

plt.title('Antiderivada Problema 25', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$F(x)$', fontsize=8)
plt.ylim(-10, 10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P25_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
