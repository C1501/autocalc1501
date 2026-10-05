import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio evitando singularidades
x = np.linspace(-1.5, 1.5, 400)

# Antiderivada con C = 0
# F(x) = x/2 - ln|sec(x/2)|
F = (x / 2.0) - np.log(np.abs(1.0 / np.cos(x / 2.0)))

plt.figure(figsize=(4, 3))
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)
plt.title(r'Gráfica de la Antiderivada (Problema 14)', fontsize=9)
plt.xlabel(r'$x$', fontsize=8)
plt.ylabel(r'$F(x)$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=8)
plt.tight_layout()

plt.savefig(r'semana_04/graficas/SEM04_P14_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
