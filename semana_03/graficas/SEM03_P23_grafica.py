import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**3 + 7*x**2 - 5*x + 5) / ((x - 1)**2 * (x**2 + 1)**2)

def F(x):
    return (np.log(np.abs(x - 1)) - (2.0 / (x - 1)) - 
            0.5 * np.log(x**2 + 1) + 3.0 * np.arctan(x) + 
            (1.0 / (x**2 + 1)))

x_vals = np.linspace(1.5, 6.0, 400)
y_f = f(x_vals)
y_F = F(x_vals)

plt.figure(figsize=(3.5, 2.5))
plt.plot(x_vals, y_f, label=r'$f(x)$', color='blue', linestyle='--')
plt.plot(x_vals, y_F, label=r'$F(x)$ con $C=0$', color='red')
plt.ylim(-5, 15)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(fontsize=8)
plt.grid(True)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P23_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
