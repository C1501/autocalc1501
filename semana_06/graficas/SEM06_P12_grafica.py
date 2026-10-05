import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3 - x**2

def F(x):
    return 3*x - (x**3)/3

x = np.linspace(0, 2, 400)
y = f(x)
y_F = F(x)

plt.figure(figsize=(6, 4))

plt.plot(x, y, label=r'$f(x) = 3 - x^2$', color='blue', linewidth=2)
plt.plot(x, y_F, label=r'$F(x)$ con $C=0$', color='red', linestyle='--', linewidth=2)

x_fill = np.linspace(0, 2, 100)
plt.fill_between(x_fill, f(x_fill), color='blue', alpha=0.2, label=r'Área $= \frac{10}{3}$')

plt.title(r'Integral Definitiva $\int_{0}^{2} (3 - x^2) dx$', fontsize=10)
plt.xlabel('$x$', fontsize=9)
plt.ylabel('$y$', fontsize=9)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='lower left', fontsize=8)

plt.tight_layout()
plt.savefig('SEM06_P12.png', dpi=300)
plt.close()
plt.savefig(r'semana_06/graficas/SEM06_P12_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
