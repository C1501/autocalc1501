import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función y su antiderivada con C=0
def f(x):
    return 1 - x**3

def F(x):
    return x - (x**4) / 4

# Configuración de los datos para el gráfico
x = np.linspace(0, 1, 400)
y = f(x)
y_F = F(x)

plt.figure(figsize=(6, 4))

# Gráfica de la función f(x)
plt.plot(x, y, 'b-', linewidth=2, label=r'$f(x) = 1 - x^3$')
# Gráfica de la antiderivada F(x) con C=0 (REGLA 8)
plt.plot(x, y_F, 'r--', linewidth=2, label=r'$F(x)$ con $C=0$')

# Sombreado bajo la curva para representar la integral definida
plt.fill_between(x, 0, y, color='blue', alpha=0.15)

plt.title(r'Interpretación Geométrica de $\int_{0}^{1} (1 - x^3) dx$', fontsize=10)
plt.xlabel('$x$', fontsize=9)
plt.ylabel('$y$', fontsize=9)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8, loc='lower left')
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.15)
plt.tight_layout()

plt.savefig(r'semana_06/graficas/SEM06_P14_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
