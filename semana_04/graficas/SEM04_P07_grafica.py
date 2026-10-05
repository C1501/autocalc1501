import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x) / (5 + 4 * np.cos(x))

def F(x):
    return x / 4 - (5 / 6) * np.arctan(np.tan(x / 2) / 3)

x = np.linspace(-2.0, 2.0, 500)
y_f = f(x)
y_F = F(x)

plt.figure(figsize=(3.5, 2.5))
plt.plot(x, y_f, label=r'$f(x)$', color='blue', linewidth=1.2)
plt.plot(x, y_F, label=r'$F(x)$ con $C=0$', color='red', linestyle='--', linewidth=1.2)

plt.title('Gráfica para SEM04_P07', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$y$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.5, linestyle=':')
plt.axvline(0, color='black', linewidth=0.5, linestyle=':')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=7, loc='best')
plt.ylim(-2, 2)
plt.tight_layout()
plt.savefig(r'semana_04/graficas/SEM04_P07_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
