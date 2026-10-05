import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x / np.sqrt(x**2 + 2*x + 2)

def F(x):
    return np.sqrt(x**2 + 2*x + 2) - np.log(x + 1 + np.sqrt(x**2 + 2*x + 2))

x = np.linspace(-3, 3, 400)
y_f = f(x)
y_F = F(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y_f, label=r'$f(x) = \frac{x}{\sqrt{x^2 + 2x + 2}}$', color='blue', linestyle='--')
plt.plot(x, y_F, label=r'$F(x)$ con $C=0$', color='red')

plt.title('Gráfica de la función y su antiderivada')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.axvline(0, color='black', linewidth=0.8, linestyle=':')
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(-4, 4)
plt.legend(loc='best', fontsize=9)
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P11_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
