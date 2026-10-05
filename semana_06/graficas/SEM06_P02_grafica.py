import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función y su antiderivada con C=0
def f(x):
    return x

def F(x):
    return 0.5 * x**2

# Configuración de los puntos para la gráfica
x_vals = np.linspace(0, 3, 400)
y_vals = f(x_vals)
F_vals = F(x_vals)

# Creación de la figura adaptada a dos columnas IEEE
fig, ax = plt.subplots(figsize=(3.5, 2.5))

# Graficar función y antiderivada
ax.plot(x_vals, y_vals, 'b-', label=r'$f(x) = x$')
ax.plot(x_vals, F_vals, 'r--', label=r'$F(x)$ con $C=0$')

# Sombreado del área bajo la curva
ax.fill_between(x_vals, 0, y_vals, alpha=0.3, color='blue')

# Configuración de ejes y etiquetas
ax.set_xlim(0, 3.2)
ax.set_ylim(0, 5)
ax.set_xlabel(r'$x$', fontsize=9)
ax.set_ylabel(r'$y$', fontsize=9)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper left', fontsize=8)

# Ajuste de diseño y guardado
plt.tight_layout()
plt.savefig('SEM06_P02_grafica.png', dpi=300)
plt.close()
plt.savefig(r'semana_06/graficas/SEM06_P02_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
