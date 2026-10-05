import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(4*x**2 + 4*x - 3)

def F(x):
    term1 = (x + 0.5) * np.sqrt(4*x**2 + 4*x - 3) / 2
    term2 = 0.5 * np.log(np.abs(x + 0.5 + np.sqrt(4*x**2 + 4*x - 3) / 2))
    return term1 - term2

x_vals = np.linspace(1.5, 4.0, 400)
y_vals = f(x_vals)
F_vals = F(x_vals)

plt.figure(figsize=(6, 4))
plt.plot(x_vals, y_vals, label=r'$f(x) = \sqrt{4x^2 + 4x - 3}$', color='blue')
plt.plot(x_vals, F_vals, label=r'$F(x)$ con $C=0$', color='red', linestyle='--')
plt.title('Gráfica de la función y su antiderivada')
plt.xlabel('x')
plt.ylabel('Y')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='best', fontsize=9)
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P47_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
