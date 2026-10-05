import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Definición de la función y la antiderivada con C=0
def f(x):
    return x

def F(x):
    return 0.5 * x**2

# Configuración del dominio
x = np.linspace(-4, 2, 400)
y_f = f(x)
y_F = F(x)

# Creación de la figura
fig, ax = plt.subplots(figsize=(3.5, 2.5))

# Graficar la función y la antiderivada
ax.plot(x, y_f, 'b-', label=r'$f(x) = x$')
ax.plot(x, y_F, 'r--', label=r'$F(x)$ con $C=0$')

# Sombra bajo la curva en el intervalo [-3, 1]
x_shade = np.linspace(-3, 1, 100)
ax.fill_between(x_shade, f(x_shade), color='gray', alpha=0.4, label=r'Área = $-4$')

# Configuración de ejes y etiquetas
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xlim([-4, 2])
ax.set_ylim([-5, 9])
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_title(r'Integral $\int_{-3}^{1} x \, dx$')
ax.legend(loc='upper left', fontsize=8)
ax.grid(True, linestyle=':', alpha=0.6)

# Ajuste de diseño
plt.tight_layout()

plt.savefig(r'semana_06/graficas/SEM06_P01_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
