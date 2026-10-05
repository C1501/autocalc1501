import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función y su antiderivada con C=0
def f(x):
    return x**(-2)

def F(x):
    return -x**(-1)

# Configuración de los datos para la gráfica
x = np.linspace(0.8, 2.2, 400)
y_f = f(x)
y_F = F(x)

# Creación de la figura adaptada para dos columnas IEEE
fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(x, y_f, label=r'$f(x) = x^{-2}$', color='blue', linewidth=1.5)
ax.plot(x, y_F, label=r'$F(x)$ con $C=0$', color='red', linestyle='--', linewidth=1.5)

# Rizado del área bajo la curva de la integral definida de 1 a 2
x_fill = np.linspace(1.0, 2.0, 200)
ax.fill_between(x_fill, f(x_fill), color='gray', alpha=0.3, label=r'Área $= 1/2$')

ax.set_xlim(0.8, 2.2)
ax.set_ylim(-1.2, 1.5)
ax.axhline(0, color='black', linewidth=0.8, linestyle='-')
ax.axvline(0, color='black', linewidth=0.8, linestyle='-')
ax.set_xlabel('$x$', fontsize=9)
ax.set_ylabel('$y$', fontsize=9)
ax.legend(fontsize=7, loc='upper right')
ax.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()

plt.savefig(r'semana_06/graficas/SEM06_P13_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
