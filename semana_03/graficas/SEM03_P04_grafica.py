import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores para x
x = np.linspace(-2, 6, 400)

# Función integrando f(x)
f = (2*x + 2) / (x**2 - 4*x + 9)

# Antiderivada F(x) con C = 0
F = np.log(x**2 - 4*x + 9) + (6 / np.sqrt(5)) * np.arctan((x - 2) / np.sqrt(5))

# Configuración de la gráfica para dos columnas IEEE
plt.figure(figsize=(3.5, 2.5))
plt.plot(x, f, 'b-', label=r'$f(x)$', linewidth=1.2)
plt.plot(x, F, 'r--', label=r'$F(x)$ con $C=0$', linewidth=1.2)

plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.title(r'Gráfica de $f(x)$ y su Antiderivada $F(x)$', fontsize=8)
plt.xlabel(r'$x$', fontsize=8)
plt.ylabel(r'$y$', fontsize=8)
plt.legend(fontsize=7, loc='upper left')
plt.grid(True, linestyle=':', alpha=0.6)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)

# Ajuste de bordes y diseño
plt.tight_layout()
plt.savefig(r'semana_03/graficas/SEM03_P04_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
