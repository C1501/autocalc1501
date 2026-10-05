import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3 * x**2 - 1

def F(x):
    return x**3 - x

x = np.linspace(-0.2, 1.2, 400)
y_f = f(x)
y_F = F(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y_f, label=r'$f(x) = 3x^2 - 1$', color='blue', linewidth=2)
plt.plot(x, y_F, label=r'$F(x)$ con $C=0$', color='red', linestyle='--', linewidth=2)

x_fill = np.linspace(0, 1, 200)
plt.fill_between(x_fill, f(x_fill), color='blue', alpha=0.2, label='Área neta = 0')

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.axvline(1, color='gray', linestyle=':', linewidth=1)

plt.title('Gráfica para el Problema 11')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper left', fontsize=9)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(-0.2, 1.2)
plt.ylim(-1.5, 1.5)
plt.tight_layout()
plt.savefig(r'semana_06/graficas/SEM06_P11_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
