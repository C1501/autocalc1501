import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir la función F(x) con C = 0
def F(x):
    return 3 * x - 4.5 * np.arctan(x) + (3 * x) / (2 * (x**2 + 1))

# Generar valores de x evitando discontinuidades (ninguna en este caso)
x = np.linspace(-3, 3, 400)
y = F(x)

# Configuración de la gráfica adaptada para dos columnas IEEE
fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(x, y, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

ax.set_title(r'Gráfica de la antiderivada $\int \frac{3x^4}{(x^2 + 1)^2} dx$', fontsize=9)
ax.set_xlabel('$x$', fontsize=8)
ax.set_ylabel('$F(x)$', fontsize=8)
ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
ax.axvline(0, color='black', linewidth=0.5, linestyle='--')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=8)
ax.tick_params(axis='both', which='major', labelsize=8)

plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P34_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
