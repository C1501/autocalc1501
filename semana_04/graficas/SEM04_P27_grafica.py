import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de la función, evitando las asíntotas donde cos(x) = 0
x = np.linspace(-1.2, 1.2, 400)

# Función original a integrar: f(x) = 1 / (1 + cos^2(x))
f_x = 1.0 / (1.0 + np.cos(x)**2)

# Antiderivada F(x) con C = 0: F(x) = (1 / sqrt(2)) * arctan(tan(x) / sqrt(2))
F_x = (1.0 / np.sqrt(2)) * np.arctan(np.tan(x) / np.sqrt(2))

plt.figure(figsize=(4, 3))
plt.plot(x, f_x, 'b-', label=r'$f(x) = \frac{1}{1+\cos^2 x}$')
plt.plot(x, F_x, 'r--', label=r'$F(x)$ con $C=0$')

plt.title('Gráfica de $f(x)$ y su Antiderivada')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', fontsize=8)
plt.tight_layout()
plt.savefig(r'semana_04/graficas/SEM04_P27_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
