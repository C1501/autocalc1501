import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio de la función (x > 0)
x = np.linspace(0.01, 6.0, 400)

# Función integrando original f(x)
f_x = 1.0 / (np.sqrt(x) + np.cbrt(x))

# Antiderivada F(x) con C = 0
F_x = 2 * np.sqrt(x) - 3 * np.cbrt(x) + 6 * (x**(1.0/6.0)) - 6 * np.log(x**(1.0/6.0) + 1)

plt.figure(figsize=(6, 4))
plt.plot(x, f_x, label=r'$f(x) = \frac{1}{\sqrt{x} + \sqrt[3]{x}}$', color='crimson', linewidth=1.5)
plt.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='navy', linestyle='--', linewidth=1.5)

plt.title('Gráfica de la función y su antiderivada (Problema 27)')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True, linestyle=':', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.ylim(-2, 8)
plt.legend(loc='upper left', fontsize=9)
plt.tight_layout()

# Ruta ajustada a la Semana 03
plt.savefig(r'semana_05/graficas/SEM05_P27_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
