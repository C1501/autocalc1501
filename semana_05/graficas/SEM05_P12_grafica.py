import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio de la función (intervalo donde 1 + x - x^2 > 0)
# Las raíces son x = (1 +- \sqrt{5})/2 aprox -0.618 y 1.618
x = np.linspace(-0.6, 1.6, 400)

# Función integrando f(x)
f = x / np.sqrt(1 + x - x**2)

# Antiderivada F(x) con C = 0
F = -np.sqrt(1 + x - x**2) + 0.5 * np.arcsin((2*x - 1) / np.sqrt(5))

plt.figure(figsize=(6, 4))
plt.plot(x, f, label=r'$f(x)$', color='blue', linestyle='--')
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='red')

plt.title(r'Gráfica del Problema 12')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.axvline(0, color='black', linewidth=0.8, linestyle=':')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='best')
plt.ylim(-2, 2)
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P12_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
