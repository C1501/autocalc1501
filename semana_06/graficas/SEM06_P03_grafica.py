import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir la función y la antiderivada con C=0
def f(x):
    return x

def F(x):
    return 0.5 * x**2  # F(x) con C=0

# Configuración de la figura para columna IEEE (ancho aprox 3.5 pulgadas)
fig, ax = plt.subplots(figsize=(3.5, 2.5))

x = np.linspace(0.5, 2.5, 200)
x_fill = np.linspace(1, 2, 100)

# Gráficas
ax.plot(x, f(x), 'b-', label=r'$f(x) = x$')
ax.plot(x, F(x), 'r--', label=r'$F(x)$ con $C=0$')

# Sombra del área bajo la curva (se evalúa sobre x_fill)
ax.fill_between(x_fill, 0, f(x_fill), color='gray', alpha=0.3, label=r'Área $= 3/2$')

# Límites y formato
ax.set_xlim(0.5, 2.5)
ax.set_ylim(0, 3)
ax.set_xlabel(r'$x$', fontsize=9)
ax.set_ylabel(r'$y$', fontsize=9)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.legend(fontsize=7, loc='upper left')
ax.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()

# Guardar ÚNICAMENTE en la carpeta de la semana 06
plt.savefig(r'semana_06/graficas/SEM06_P03_grafica.png', dpi=300, bbox_inches='tight')
plt.close()