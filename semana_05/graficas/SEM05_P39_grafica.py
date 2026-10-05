import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.5, 1.0, 400)
f_x = (x**2) / ((3 + x)**(-5/3))

# Antiderivada con C = 0
F_x = (3/14)*(3 + x)**(14/3) - (18/11)*(3 + x)**(11/3) + (27/8)*(3 + x)**(8/3)

fig, ax = plt.subplots(figsize=(4, 3))
ax.plot(x, f_x, label=r'$f(x)$', color='blue', linewidth=1.5)
ax.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='red', linestyle='--', linewidth=1.5)

ax.set_title('Gráfica de f(x) y su Antiderivada')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.axhline(0, color='black', linewidth=0.5, linestyle=':')
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(fontsize=8)

plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P39_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
