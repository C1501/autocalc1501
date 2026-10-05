import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

a = 1.0
b = 3.0
x = np.linspace(a, b, 400)
f_x = x**-2
F_x = -1.0 / x

plt.figure(figsize=(6, 4))
plt.plot(x, f_x, 'b-', label=r'$f(x) = x^{-2}$')
plt.plot(x, F_x, 'r--', label=r'$F(x)$ con $C=0$')
plt.fill_between(x, 0, f_x, color='blue', alpha=0.15, label='Área bajo la curva')

plt.title(r'Interpretación Geométrica de $\int_{a}^{b} x^{-2} dx$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.legend(loc='upper right', fontsize=9)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.savefig(r'semana_06/graficas/SEM06_P16_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
