import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Configuración de estilo para IEEE (ancho de columna en pulgadas ~3.5)
fig, ax = plt.subplots(figsize=(3.5, 2.5))

# Definir función y antiderivada con C=0
def f(x):
    return x

def F(x):
    return 0.5 * x**2  # F(x) con C = 0

# Generar puntos para las gráficas
x_vals = np.linspace(-2.5, 3.5, 400)
x_fill = np.linspace(-2, 3, 200)

# Graficar la función f(x) y la antiderivada F(x)
ax.plot(x_vals, f(x_vals), label=r'$f(x) = x$', color='blue')
ax.plot(x_vals, F(x_vals), label=r'$F(x)$ con $C=0$', color='red', linestyle='--')

# Sombrear el área de la integral definida desde x = -2 hasta x = 3
ax.fill_between(x_fill, 0, f(x_fill), color='gray', alpha=0.4, label=r'Integral $= 5/2$')

# Configuración de ejes y etiquetas
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xlim([-2.5, 3.5])
ax.set_ylim([-3, 6])
ax.set_xlabel(r'$x$', fontsize=9)
ax.set_ylabel(r'$y$', fontsize=9)
ax.legend(fontsize=7, loc='upper left')
ax.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()

# Guardar en la carpeta de la Semana 06
plt.savefig(r'semana_06/graficas/SEM06_P04_grafica.png', dpi=300, bbox_inches='tight')
plt.close()