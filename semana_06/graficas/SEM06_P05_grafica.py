import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función y su antiderivada con C=0
def f(x):
    return x**3 - 1

def F(x):
    return (x**4 / 4) - x

# Generar datos para la gráfica
x = np.linspace(0, 1, 400)
y = f(x)
y_F = F(x)

plt.figure(figsize=(6, 4))

# Graficar la función integrando
plt.plot(x, y, label=r'$f(x) = x^3 - 1$', color='blue', linewidth=2)

# Graficar la antiderivada especificando C = 0 en la leyenda
plt.plot(x, y_F, label=r'$F(x)$ con $C=0$', color='red', linestyle='--', linewidth=2)

# Rellenar el área bajo la curva en el intervalo [0, 1]
plt.fill_between(x, y, 0, color='blue', alpha=0.15, label=r'Área = $-3/4$')

# Configuración de ejes y etiquetas
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title(r'Interpretación Geométrica: $\int_{0}^{1} (x^3 - 1) dx$', fontsize=10)
plt.xlabel('$x$', fontsize=9)
plt.ylabel('$y$', fontsize=9)
plt.legend(loc='lower left', fontsize=8)
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()

plt.savefig(r'semana_06/graficas/SEM06_P05_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
