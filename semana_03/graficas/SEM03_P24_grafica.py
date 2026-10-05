import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*x / (x**2 + x + 1)**2

def F(x):
    return -(2*x + 1) / (3*(x**2 + x + 1)) - (4*np.sqrt(3)/9) * np.arctan((2*x + 1)/np.sqrt(3))

x_vals = np.linspace(-3.0, 3.0, 400)
y_f = f(x_vals)
y_F = F(x_vals)

plt.figure(figsize=(6, 4))
plt.plot(x_vals, y_f, label=r'$f(x) = \frac{2x}{(x^2+x+1)^2}$', color='crimson', linewidth=1.5)
plt.plot(x_vals, y_F, label=r'$F(x)$ con $C=0$', color='navy', linestyle='--', linewidth=1.5)

plt.axhline(0, color='black', linewidth=0.8, linestyle='-')
plt.axvline(0, color='black', linewidth=0.8, linestyle='-')
plt.title('Gráfica de la función y su antiderivada (Problema 24)')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.ylim(-2.5, 2.5)
plt.legend(loc='upper right', fontsize=9)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P24_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
