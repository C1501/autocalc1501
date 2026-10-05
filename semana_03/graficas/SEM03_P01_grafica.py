import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores para x
x = np.linspace(-4, 3, 400)

# Función integrand f(x)
f = 1 / (4*x**2 + 4*x + 10)

# Antiderivada F(x) evaluada con C = 0
F = (1/6) * np.arctan((2*x + 1) / 3)

# Crear la gráfica adaptada a dos columnas (ancho compacto)
plt.figure(figsize=(3.5, 2.5))

plt.plot(x, f, label=r'$f(x)$', color='tab:blue', linestyle='--')
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='tab:orange', linewidth=2)

plt.title(r'Gráfica de $f(x)$ y su Antiderivada $F(x)$', fontsize=9)
plt.xlabel(r'$x$', fontsize=8)
plt.ylabel(r'$y$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)

plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P01_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
