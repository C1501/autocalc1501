import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x + 2) / (x**2 + 2*x + 2)

def F(x):
    return 0.5 * np.log(x**2 + 2*x + 2) + np.arctan(x + 1)

x = np.linspace(-4, 2, 400)
y_f = f(x)
y_F = F(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y_f, label=r'$f(x)$ (Integrando)', color='blue', linestyle='--')
plt.plot(x, y_F, label=r'$F(x)$ con $C=0$', color='red')

plt.title('Gráfica de la función y su antiderivada')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.axvline(0, color='black', linewidth=0.8, linestyle=':')
plt.ylim(-2, 4)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left', fontsize=9)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P06_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
