import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi, 400)
y_integrand = np.cos(x)
y_antideriv = np.sin(x)  # F(x) con C = 0

fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(x, y_integrand, label=r'$f(x) = \cos(x)$', color='blue')
ax.plot(x, y_antideriv, label=r'$F(x)$ con $C=0$', color='red', linestyle='--')
ax.axhline(0, color='black', linewidth=0.8, linestyle=':')

ax.fill_between(x, 0, y_integrand, where=((x >= 0) & (x <= np.pi)), 
                color='gray', alpha=0.3, label='Área neta = 0')

ax.set_title(r'Integral de $\cos(x)$ en $[0, \pi]$', fontsize=9)
ax.set_xlabel('$x$', fontsize=8)
ax.set_ylabel('$y$', fontsize=8)
ax.legend(fontsize=7, loc='upper right')
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()

plt.savefig(r'semana_06/graficas/SEM06_P15_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
