import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de la función, evitando las asíntotas y discontinuidades
x = np.linspace(-1.2, 1.2, 400)

# Definir la función integrando f(x)
f = 1.0 / (1.0 + np.sin(x)**2)

# Definir la antiderivada F(x) con C = 0
F = (np.sqrt(2) / 2.0) * np.arctan(np.sqrt(2) * np.tan(x))

plt.figure(figsize=(4, 3))
plt.plot(x, f, label=r'$f(x) = \frac{1}{1 + \sin^2 x}$', color='blue')
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='red', linestyle='--')

plt.title('Gráfica de f(x) y su Antiderivada')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.axvline(0, color='black', linewidth=0.8, linestyle=':')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=8)
plt.tight_layout()

plt.savefig(r'semana_04/graficas/SEM04_P26_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
