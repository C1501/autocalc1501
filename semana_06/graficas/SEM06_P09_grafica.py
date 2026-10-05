import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir la función a integrar
def f(x):
    return 4 - x**2

# Definir la antiderivada F(x) con C = 0
# F(x) = 4x - (x^3)/3
def F(x):
    return 4*x - (x**3)/3

# Configurar datos para la gráfica
x = np.linspace(0.5, 2.5, 400)
y = f(x)
y_anti = F(x) - F(1) # Ajustada para visualización geométrica en [1,2]
y_anti_c0 = F(x)     # Antiderivada pura con C = 0

plt.figure(figsize=(6, 4))

# Graficar la función y la antiderivada
plt.plot(x, y, 'b-', label=r'$f(x) = 4 - x^2$', linewidth=2)
plt.plot(x, y_anti_c0, 'g--', label=r'$F(x)$ con $C=0$', linewidth=2)

# Sombrear el área bajo la curva de 1 a 2
x_fill = np.linspace(1, 2, 200)
plt.fill_between(x_fill, f(x_fill), color='orange', alpha=0.4, label=r'Área $= \frac{5}{3}$')

# Configuración de la gráfica
plt.title(r'Interpretación Geométrica de $\int_{1}^{2} (4 - x^2) dx$', fontsize=10)
plt.xlabel('$x$', fontsize=9)
plt.ylabel('$y$', fontsize=9)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlim(0.5, 2.5)
plt.ylim(-1, 5)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right', fontsize=8)

plt.tight_layout()

plt.savefig(r'semana_06/graficas/SEM06_P09_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
