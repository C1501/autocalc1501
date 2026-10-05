import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función F(x) con C = 0
def F(x):
    return (1.0 / 16.0) * np.arcsin(x) + (x * np.sqrt(1 - x**2) / 48.0) * (2 * x**4 - x**2 - 2)

# Dominio de la función [-1, 1] debido a la raíz y arcoseno
x = np.linspace(-0.99, 0.99, 400)
y = F(x)

# Configuración de la gráfica para formato IEEE (ancho de columna)
plt.figure(figsize=(3.5, 2.5))
plt.plot(x, y, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

plt.title(r'Gráfica de la antiderivada $F(x)$', fontsize=9)
plt.xlabel(r'$x$', fontsize=8)
plt.ylabel(r'$F(x)$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)

plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P25_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
