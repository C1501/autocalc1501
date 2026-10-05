import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (5 * x + 4) / np.sqrt(x**2 + 2*x + 5)

def F(x):
    return 5 * np.sqrt(x**2 + 2*x + 5) - np.log(np.abs(x + 1 + np.sqrt(x**2 + 2*x + 5)))

x = np.linspace(-3, 3, 400)
y_integrand = f(x)
y_antideriv = F(x) # C = 0

plt.figure(figsize=(6, 4))
plt.plot(x, y_integrand, label=r'Integrando $\frac{5x+4}{\sqrt{x^2+2x+5}}$', color='blue', linewidth=1.5)
plt.plot(x, y_antideriv, label=r'$F(x)$ con $C=0$', color='red', linestyle='--', linewidth=1.5)

plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.axvline(0, color='black', linewidth=0.8, linestyle=':')
plt.title('Gráfica del Problema 14', fontsize=10)
plt.xlabel('$x$', fontsize=9)
plt.ylabel('$y$', fontsize=9)
plt.ylim(-10, 20)
plt.legend(fontsize=8)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P14_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
