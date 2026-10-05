import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir la función y su antiderivada con C=0
def f(x):
    return x

def F(x):
    return 0.5 * x**2

# Configurar datos para la gráfica
x = np.linspace(-1.5, 1.5, 400)
y_f = f(x)
y_F = F(x)

# Crear la figura apta para dos columnas IEEE
fig, ax = plt.subplots(figsize=(3.5, 2.5))

# Graficar curvas
ax.plot(x, y_f, 'b-', label=r'$f(x) = x$')
ax.plot(x, y_F, 'r--', label=r'$F(x)$ con $C=0$')

# Sombrear el área bajo la curva de -1 a 1
x_fill = np.linspace(-1, 1, 100)
ax.fill_between(x_fill, f(x_fill), color='gray', alpha=0.3, label=r'Área $= 0$')

# Configurar ejes y etiquetas
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.2, 1.5])
ax.set_xlabel(r'$x$', fontsize=9)
ax.set_ylabel(r'$y$', fontsize=9)
ax.legend(loc='upper left', fontsize=7)
ax.grid(True, linestyle=':', alpha=0.6)

# Ajustar diseño
plt.tight_layout()

plt.savefig(r'semana_06/graficas/SEM06_P07_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
