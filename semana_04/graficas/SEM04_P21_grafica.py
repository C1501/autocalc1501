import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de la función, evitando las asíntotas donde sin(x) = sqrt(2) (lo cual no ocurre en los reales)
x = np.linspace(-1.5, 1.5, 400)

# Función integrando f(x)
f = np.cos(x) / (np.cos(x)**2 + 1)

# Antiderivada F(x) con C = 0
F = (np.sqrt(2) / 4) * np.log(np.abs((np.sqrt(2) + np.sin(x)) / (np.sqrt(2) - np.sin(x))))

plt.figure(figsize=(6, 4))
plt.plot(x, f, label=r'$f(x) = \frac{\cos x}{\cos^2 x + 1}$', color='blue', linestyle='--')
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='red')

plt.title('Gráfica del Integrando y su Antiderivada')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(0, color='black', linewidth=0.8, linestyle='-')
plt.axvline(0, color='black', linewidth=0.8, linestyle='-')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='best', fontsize=9)
plt.tight_layout()
plt.savefig(r'semana_04/graficas/SEM04_P21_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
