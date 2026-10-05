import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio evitando las asíntotas y singularidades
x = np.linspace(-1.5, 1.5, 400)

# Función original f(x)
den = 1.0 - np.cos(x) + np.sin(x)
f = np.sin(x) / den

# Antiderivada F(x) con C = 0
F = np.log(np.abs(np.tan(x / 2.0) + 1.0))

plt.figure(figsize=(3.5, 2.5))
plt.plot(x, f, 'b-', label=r'$f(x)$', linewidth=1.2)
plt.plot(x, F, 'r--', label=r'$F(x)$ con $C=0$', linewidth=1.2)

plt.ylim(-4, 4)
plt.xlabel(r'$x$', fontsize=9)
plt.ylabel(r'$y$', fontsize=9)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8, loc='upper left')
plt.tight_layout()

plt.savefig(r'semana_04/graficas/SEM04_P09_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
