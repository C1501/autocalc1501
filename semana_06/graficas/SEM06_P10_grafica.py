import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1.5, 3.5, 400)
y = x

# Antiderivada F(x) con C = 0
F = (x**2) / 2

fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(x, y, 'b-', label=r'$f(x) = x$')
ax.plot(x, F, 'r--', label=r'$F(x)$ con $C=0$')

# Sombreado bajo la curva de 2 a 3
x_fill = np.linspace(2, 3, 100)
ax.fill_between(x_fill, 0, x_fill, color='gray', alpha=0.4, label=r'Área $= \frac{5}{2}$')

ax.set_xlim(1.5, 3.5)
ax.set_ylim(0, 6)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.legend(loc='upper left', fontsize=8)
ax.grid(True, linestyle=':', alpha=0.6)

plt.tight_confinement = True if 'tight_confinement' in globals() else None
plt.savefig(r'semana_06/graficas/SEM06_P10_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
