import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de la función, evitando posibles singularidades reales (no las hay en x^2+1)
x = np.linspace(-3, 3, 400)

# Antiderivada F(x) con C = 0
# F(x) = x - 1.5 * arctan(x) + x / (2 * (x^2 + 1))
F = x - 1.5 * np.arctan(x) + x / (2 * (x**2 + 1))

# Configuración de la gráfica adaptada a dos columnas IEEE
fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(x, F, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

ax.set_title(r'Antiderivada del Problema 11', fontsize=9)
ax.set_xlabel(r'$x$', fontsize=8)
ax.set_ylabel(r'$F(x)$', fontsize=8)
ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
ax.axvline(0, color='black', linewidth=0.5, linestyle='--')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=8)
ax.tick_params(axis='both', labelsize=7)

plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P11_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
