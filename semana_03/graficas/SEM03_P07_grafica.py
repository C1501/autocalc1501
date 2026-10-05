import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.5, 1.8, 400)
# Evitar división por cero en x = 2 (fuera del dominio graficado)
y = np.log(np.abs(x - 2)) - 2.0 / (x - 2)

plt.figure(figsize=(3.5, 2.5))
plt.plot(x, y, 'b-', label=r'$F(x)$ con $C=0$')
plt.axvline(x=2, color='r', linestyle='--', alpha=0.5, label=r'Asintota $x=2$')
plt.title(r'Grafica de $F(x) = \ln|x-2| - \frac{2}{x-2}$', fontsize=9)
plt.xlabel(r'$x$', fontsize=8)
plt.ylabel(r'$F(x)$', fontsize=8)
plt.ylim(-10, 5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend(fontsize=7, loc='lower right')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P07_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
