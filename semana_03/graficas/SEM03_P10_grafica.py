import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**3 + x**2 + x + 3) / (x**4 + 4*x**2 + 3)

def F(x):
    return np.arctan(x) + 0.5 * np.log(x**2 + 3)

x_vals = np.linspace(-3, 3, 400)
y_f = f(x_vals)
y_F = F(x_vals)

plt.figure(figsize=(6, 4))
plt.plot(x_vals, y_f, label=r'Integrando $f(x)$', color='blue', linestyle='--')
plt.plot(x_vals, y_F, label=r'$F(x)$ con $C=0$', color='red')

plt.title('Gráfica de la función y su antiderivada')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(0, color='black', linewidth=0.8, linestyle='-')
plt.axvline(0, color='black', linewidth=0.8, linestyle='-')
plt.ylim(-2, 5)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', fontsize=9)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P10_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
