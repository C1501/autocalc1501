import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

alpha = np.pi / 4
x = np.linspace(-2.5, 2.5, 400)

def integrand(x_val):
    return 1.0 / np.sqrt(x_val**2 + 2*x_val*np.cos(alpha) + 1.0)

def antiderivative(x_val):
    return np.log(np.abs(x_val + np.cos(alpha) + np.sqrt(x_val**2 + 2*x_val*np.cos(alpha) + 1.0)))

y_integ = integrand(x)
y_antid = antiderivative(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y_integ, label=r'Integrando $f(x)$', color='blue', linestyle='--')
plt.plot(x, y_antid, label=r'$F(x)$ con $C=0$', color='red', linewidth=2)

plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.title(r'Solucion para $\alpha = \pi/4$', fontsize=10)
plt.xlabel('$x$', fontsize=9)
plt.ylabel('$y$', fontsize=9)
plt.legend(fontsize=8, loc='best')
plt.grid(True, linestyle=':', alpha=0.6)
plt.ylim(-2, 3)
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P23_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
