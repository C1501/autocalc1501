import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función y la antiderivada con C=0
def f(x):
    return x**2 - 2*x + 2

def F(x):
    return (x**3)/3 - x**2 + 2*x

# Configuración del intervalo
a, b = -2, 2
x_vals = np.linspace(a - 0.5, b + 0.5, 400)
y_vals = f(x_vals)
F_vals = F(x_vals)

# Generación de la gráfica adaptada a IEEE (ancho de columna)
plt.figure(figsize=(3.5, 2.5))
plt.plot(x_vals, y_vals, 'b-', label=r'$f(x) = x^2 - 2x + 2$')
plt.plot(x_vals, F_vals, 'r--', label=r'$F(x)$ con $C=0$')

# Sombreado del área bajo la curva
x_fill = np.linspace(a, b, 200)
plt.fill_between(x_fill, f(x_fill), color='gray', alpha=0.3, label='Área = 40/3')

plt.title('Gráfica para Problema 18', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$y$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend(fontsize=7, loc='upper center')
plt.grid(True, linestyle=':', alpha=0.6)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()

plt.savefig(r'semana_06/graficas/SEM06_P18_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
