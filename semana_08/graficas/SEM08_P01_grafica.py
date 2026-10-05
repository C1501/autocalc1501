import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(0.05, 10, 400)
y_vals_div = np.log(x_vals) / x_vals
y_vals_log = np.log(x_vals)

plt.figure(figsize=(3.5, 2.5))
plt.plot(x_vals, y_vals_div, label=r'$\frac{\ln(x)}{x}$', color='blue')
plt.plot(x_vals, y_vals_log, label=r'$\ln(x)$ con $C=0$', color='red', linestyle='--')

plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.xlim(0, 10)
plt.ylim(-4, 3)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Comportamiento de límites')
plt.legend(fontsize=8, loc='best')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig(r'semana_08/graficas/SEM08_P01_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
