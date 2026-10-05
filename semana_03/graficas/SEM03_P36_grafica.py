import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio de la función, evitando la asíntota en x = 1
x1 = np.linspace(-3, 0.95, 400)
x2 = np.linspace(1.05, 4, 400)
x = np.concatenate([x1, x2])

# Antiderivada F(x) con C = 0
def F(x_val):
    term1 = (3/25) * np.log(np.abs(x_val - 1))
    term2 = (47/50) * np.log(x_val**2 + 2*x_val + 2)
    term3 = -(107/50) * np.arctan(x_val + 1)
    term4 = -3 / (5 * (x_val**2 + 2*x_val + 2))
    return term1 + term2 + term3 + term4

y = F(x)

# Configuración de la gráfica adaptada a dos columnas IEEE
plt.figure(figsize=(3.5, 2.5))
plt.plot(x, y, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)
plt.axvline(x=1, color='r', linestyle='--', alpha=0.6, label='Asíntota $x=1$')

plt.title(r'Antiderivada del Problema 36', fontsize=9)
plt.xlabel(r'$x$', fontsize=8)
plt.ylabel(r'$F(x)$', fontsize=8)
plt.ylim(-6, 2)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=7, loc='lower right')
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P36_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
