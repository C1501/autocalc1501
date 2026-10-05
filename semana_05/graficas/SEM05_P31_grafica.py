import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.5, 2.0, 400)
# F(x) con C = 0 -> (2/3)*(4 + x^3)**(1/2)
# Nota: para x en [-1.5, 2.0], 4 + x^3 es positivo (4 - 3.375 > 0)
y_F = (2.0 / 3.0) * (4.0 + x**3)**(0.5)

# Derivada / Integrando f(x)
y_f = (x**2) / np.sqrt(4.0 + x**3)

plt.figure(figsize=(3.5, 2.8))
plt.plot(x, y_F, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)
plt.plot(x, y_f, label=r'$f(x) = \frac{x^2}{\sqrt{4+x^3}}$', color='r', linestyle='--', linewidth=1.2)

plt.title('Antiderivada e Integrando (Prob 31)', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$y$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.axvline(0, color='black', linewidth=0.8, linestyle=':')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=7, loc='upper left')
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()
plt.savefig(r'semana_05/graficas/SEM05_P31_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
