import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(x**2 + x + 1)

def F(x):
    term1 = (2*x + 1) / 4.0 * np.sqrt(x**2 + x + 1)
    arg = (2 * np.sqrt(x**2 + x + 1) + (2*x + 1)) / np.sqrt(3)
    term2 = 3.0 / 8.0 * np.log(np.abs(arg))
    return term1 + term2

x = np.linspace(-2.0, 2.0, 400)
y_integrand = f(x)
y_antideriv = F(x)

plt.figure(figsize=(3.5, 2.5))
plt.plot(x, y_integrand, label=r'$f(x) = \sqrt{x^2+x+1}$', color='blue', linewidth=1.5)
plt.plot(x, y_antideriv, label=r'$F(x)$ con $C=0$', color='red', linestyle='--', linewidth=1.5)

plt.title(r'Gráfica para el Problema 17', fontsize=9)
plt.xlabel(r'$x$', fontsize=8)
plt.ylabel(r'$y$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.axvline(0, color='black', linewidth=0.8, linestyle=':')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=7, loc='upper center')
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()
plt.savefig(r'semana_05/graficas/SEM05_P17_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
