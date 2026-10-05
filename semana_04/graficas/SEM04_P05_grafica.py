import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio para x, evitando las asíntotas en x = 0 y múltiplos de 2pi
x = np.linspace(0.5, 5.5, 400)

# Antiderivada F(x) con C = 0
# F(x) = -cot(x/2)
F_x = -1.0 / np.tan(x / 2.0)

plt.figure(figsize=(3.5, 2.5))
plt.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

plt.title(r'Antiderivada de $\int \frac{dx}{1 - \cos x}$', fontsize=9)
plt.xlabel(r'$x$', fontsize=8)
plt.ylabel(r'$F(x)$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.ylim(-6, 6)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8, loc='upper right')
plt.tight_layout()


plt.savefig(r'semana_04/graficas/SEM04_P05_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
