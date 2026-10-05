import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (2*x**2 - 3*x + 5) / ((x + 2)*(x - 1)*(x - 3))

def F(x):
    return (19/15)*np.log(np.abs(x + 2)) - (2/3)*np.log(np.abs(x - 1)) + (7/5)*np.log(np.abs(x - 3))

x = np.linspace(-1.5, 0.5, 1000)
y = f(x)
y_ant = F(x)

fig, ax = plt.subplots(figsize=(3.5, 2.5))
ax.plot(x, y, label=r'$f(x)$', color='blue', linewidth=1.2)
ax.plot(x, y_ant, label=r'$F(x)$ con $C=0$', color='red', linestyle='--', linewidth=1.2)

ax.set_ylim(-10, 10)
ax.set_xlabel('$x$', fontsize=8)
ax.set_ylabel('$y$', fontsize=8)
ax.axhline(0, color='black', linewidth=0.8, linestyle=':')
ax.legend(fontsize=7, loc='best')
ax.grid(True, linestyle='--', alpha=0.5)
ax.tick_params(axis='both', labelsize=7)

plt.tight_layout()
plt.savefig('output_plot.png', dpi=300)
plt.savefig(r'semana_03/graficas/SEM03_P26_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
