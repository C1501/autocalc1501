import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio de la función
x = np.linspace(-0.9, 4.0, 400)

# Antiderivada F(x) con C = 0
# F(x) = -ln(x+1) + (3/2)*ln(x^2+x+2) - (1/sqrt(7))*arctan((2x+1)/sqrt(7))
y = -np.log(x + 1) + 1.5 * np.log(x**2 + x + 2) - (1.0 / np.sqrt(7)) * np.arctan((2*x + 1) / np.sqrt(7))

plt.figure(figsize=(6, 4))
plt.plot(x, y, label=r'$F(x)$ con $C=0$', color='b', linewidth=2)
plt.title(r'Gráfica de la Antiderivada (Problema 31)')
plt.xlabel(r'$x$')
plt.ylabel(r'$F(x)$')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P31_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
