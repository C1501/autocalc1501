import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio para x (evitando valores negativos por la raíz cuarta)
x = np.linspace(0.01, 4.0, 400)

# Antiderivada F(x) con C = 0
# F(x) = -2*sqrt(x) + 4*root4(x) - 4*ln(1 + root4(x))
F = -2 * np.sqrt(x) + 4 * (x**0.25) - 4 * np.log(1 + x**0.25)

plt.figure(figsize=(3.5, 2.5))
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)
plt.title('Gráfica de la Antiderivada', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$F(x)$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P01_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
