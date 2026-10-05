import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del rango de x evitando las asíntotas y discontinuidades
x = np.linspace(-2.0, 2.0, 600)

# Función integrando original f(x)
def integrand(x):
    sin_x = np.sin(x)
    cos_x = np.cos(x)
    denom = sin_x - cos_x + 1.0
    # Evitar división por cero cercana a las asíntotas
    return np.where(np.abs(denom) > 1e-4, 1.0 / denom, np.nan)

# Antiderivada F(x) con C = 0
def antiderivative(x):
    z = np.tan(x / 2.0)
    # Usamos la forma logarítmica equivalente derivada
    val = z / (z + 1.0)
    return np.where(val > 0, np.log(np.abs(val)), np.nan)

y_integrand = integrand(x)
y_antideriv = antiderivative(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y_integrand, label=r'$f(x) = \frac{1}{\sin x - \cos x + 1}$', color='crimson', linestyle='--')
plt.plot(x, y_antideriv, label=r'$F(x)$ con $C=0$', color='dodgerblue', linewidth=2)

plt.title('Gráfica de la función y su antiderivada')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.ylim(-6, 6)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', fontsize=9)
plt.tight_layout()

plt.savefig(r'semana_04/graficas/SEM04_P29_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
