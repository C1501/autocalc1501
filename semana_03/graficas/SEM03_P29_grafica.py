import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio para x
x = np.linspace(-0.9, 4.0, 400)

# Antiderivada F(x) con C = 0
F = np.log(np.abs(x + 1)) + 0.5 * np.log(x**2 + 2*x + 2) - np.arctan(x + 1) - 1.0 / (2 * (x**2 + 2*x + 2))

plt.figure(figsize=(6, 4))
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='b', linewidth=2)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(-1, color='red', linewidth=0.8, linestyle=':', label='Asintota $x = -1$')

plt.title('Grafica de la antiderivada (Problema 29)')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.ylim(-3, 3)
plt.legend(loc='lower right')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.savefig(r'semana_03/graficas/SEM03_P29_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
