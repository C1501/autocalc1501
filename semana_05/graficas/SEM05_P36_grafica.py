import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.5, 4.0, 400)

# Antiderivada con C = 0
# F(x) = (4/3)*(16 + x^5)**(3/4) - 16*(16 + x^5)**(-1/4)
F = (4.0 / 3.0) * (16.0 + x**5)**(0.75) - 16.0 * (16.0 + x**5)**(-0.25)

plt.figure(figsize=(3.5, 2.5))
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

plt.title('Gráfica de la Antiderivada', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$F(x)$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P36_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
