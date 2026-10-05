import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio para la gráfica en la columna estrecha
x = np.linspace(-6, 2, 400)

# Función integrando
integrando = (2 * x - 3) / (x**2 + 6 * x + 15)

# Antiderivada F(x) con C = 0
F_x = np.log(x**2 + 6 * x + 15) - (3 * np.sqrt(6) / 2) * np.arctan((x + 3) / np.sqrt(6))

plt.figure(figsize=(3.5, 2.5))
plt.plot(x, integrando, label=r'Integrando $\frac{2x-3}{x^2+6x+15}$', color='crimson', linestyle='--')
plt.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='navy', linewidth=2)

plt.title('Gráfica de la solución (Problema 03)', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$y$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.5, linestyle=':')
plt.axvline(0, color='black', linewidth=0.5, linestyle=':')
plt.legend(fontsize=7, loc='best')
plt.grid(True, linestyle=':', alpha=0.6)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()
plt.savefig(r'semana_03/graficas/SEM03_P03_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
