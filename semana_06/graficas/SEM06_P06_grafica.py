import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir la función integranda f(x) = 3x - x^3
def f(x):
    return 3 * x - x**3

# Definir la antiderivada F(x) = (3/2)x^2 - (1/4)x^4 con C=0
def F(x):
    return 1.5 * x**2 - 0.25 * x**4

# Configuración del mallado para el gráfico
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
y_antideriv = F(x)

# Creación de la figura adaptada para dos columnas en IEEE
fig, ax = plt.subplots(figsize=(3.5, 2.5))

# Graficar la función y la antiderivada
ax.plot(x, y, label=r'$f(x) = 3x - x^3$', color='b', linewidth=1.5)
ax.plot(x, y_antideriv, label=r'$F(x)$ con $C=0$', color='r', linestyle='--', linewidth=1.5)

# Riquetear el área bajo la curva de 0 a 2
x_fill = np.linspace(0, 2, 200)
ax.fill_between(x_fill, f(x_fill), color='gray', alpha=0.3, label=r'Área $= 2$')

# Configuración de ejes y etiquetas
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(-2, 4)
ax.axhline(0, color='black', linewidth=0.8, linestyle='-')
ax.axvline(0, color='black', linewidth=0.8, linestyle='-')
ax.set_xlabel('$x$', fontsize=9)
ax.set_ylabel('$y$', fontsize=9)
ax.legend(fontsize=7, loc='upper right')
ax.grid(True, linestyle=':', alpha=0.6)

# Ajustar diseño
plt.tight_layout()

plt.savefig(r'semana_06/graficas/SEM06_P06_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
