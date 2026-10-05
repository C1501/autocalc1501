import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Definición de la función y su antiderivada con C=0
def f(x):
    return x**2 - x**3

def F(x):
    return (x**3)/3 - (x**4)/4

# Puntos para la gráfica
x = np.linspace(0, 1, 400)
y_f = f(x)
y_F = F(x)

# Configuración de la figura para IEEE (ancho de una columna aprox. 3.5 pulgadas)
plt.figure(figsize=(3.5, 2.5))

plt.plot(x, y_f, 'b-', label=r'$f(x) = x^2 - x^3$')
plt.plot(x, y_F, 'r--', label=r'$F(x)$ con $C=0$')

plt.fill_between(x, 0, y_f, color='blue', alpha=0.15)

plt.title(r'$\int_{0}^{1} (x^2 - x^3) \, dx = \frac{1}{12}$', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$y$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=7, loc='upper right')

plt.tight_layout()

plt.savefig(r'semana_06/graficas/SEM06_P17_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
