import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio evitando la asíntota en x = 1
x1 = np.linspace(-2, 0.9, 400)
x2 = np.linspace(1.1, 4, 400)
x = np.concatenate([x1, x2])

# Función antiderivada F(x) con C = 0
def F(x):
    term1 = -1/25 * np.log(np.abs(x - 1))
    term2 = 13/25 * np.log(x**2 + 2*x + 2)
    term3 = -17 / (5 * (x - 1))
    term4 = -3 / (5 * (x - 1)**2)
    term5 = -51/25 * np.arctan(x + 1)
    return term1 + term2 + term3 + term4 + term5

y = F(x)

# Acotar valores extremos para una visualización limpia
y[np.abs(y) > 20] = np.nan

plt.figure(figsize=(6, 4))
plt.plot(x, y, label=r'$F(x)$ con $C=0$', color='blue', linewidth=1.5)
plt.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='Asíntota $x=1$')

plt.title('Antiderivada del Problema 32', fontsize=10)
plt.xlabel('$x$', fontsize=9)
plt.ylabel('$F(x)$', fontsize=9)
plt.ylim(-15, 10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P32_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
