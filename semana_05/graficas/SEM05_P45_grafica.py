import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio para x > 1
x = np.linspace(1.01, 6.0, 400)

# Función original a integrar f(x)
y_orig = x / np.sqrt(x - 1)

# Antiderivada F(x) con C = 0
y_anti = (2.0 / 3.0) * (x - 1)**(1.5) + 2.0 * np.sqrt(x - 1)

plt.figure(figsize=(6, 4))
plt.plot(x, y_orig, label=r'$f(x) = \frac{x}{\sqrt{x-1}}$', color='blue', linewidth=1.5)
plt.plot(x, y_anti, label=r'$F(x)$ con $C=0$', color='red', linestyle='--', linewidth=1.5)

plt.title('Gráfica de $f(x)$ y su Antiderivada $F(x)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(1, color='gray', linewidth=0.8, linestyle=':', label='Asíntota $x=1$')
plt.ylim(-1, 15)
plt.legend(loc='upper left', fontsize=9)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.savefig(r'semana_05/graficas/SEM05_P45_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
