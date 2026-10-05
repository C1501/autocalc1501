import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de x
x = np.linspace(-3.0, 1.0, 400)

# Calcular el integrando f(x)
f_x = np.sqrt(x**2 + 2*x + 2)

# Calcular la antiderivada F(x) con C = 0
F_x = ((x + 1) / 2.0) * np.sqrt(x**2 + 2*x + 2) + 0.5 * np.log(np.abs(x + 1 + np.sqrt(x**2 + 2*x + 2)))

plt.figure(figsize=(6, 4))
plt.plot(x, f_x, label=r'$f(x) = \sqrt{x^2+2x+2}$', color='blue', linewidth=1.5)
plt.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='red', linestyle='--', linewidth=1.5)

plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.axvline(0, color='black', linewidth=0.8, linestyle=':')
plt.title(r'Gráfica para el Problema 18', fontsize=10)
plt.xlabel('$x$', fontsize=9)
plt.ylabel('$y$', fontsize=9)
plt.legend(fontsize=8)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim([-3.0, 1.0])
plt.ylim([-0.5, 4.0])
plt.tight_layout()
plt.savefig(r'semana_05/graficas/SEM05_P18_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
