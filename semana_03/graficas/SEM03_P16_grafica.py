import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores para x (evitando la asíntota en x = -1)
x1 = np.linspace(-3, -1.05, 400)
x2 = np.linspace(-0.95, 4, 400)
x = np.concatenate([x1, x2])

# Definir la función integrando f(x)
def integrand(val):
    return (val**2 + 1) / (val**3 + 1)

# Definir la antiderivada F(x) con C = 0
def antiderivative(val):
    term1 = (2/3) * np.log(np.abs(val + 1))
    term2 = (1/6) * np.log(np.abs(val**2 - val + 1))
    term3 = (np.sqrt(3)/3) * np.arctan((2*val - 1) / np.sqrt(3))
    return term1 + term2 + term3

y_integrand = integrand(x)
y_antideriv = antiderivative(x)

# Configuración de la gráfica para formato IEEE de dos columnas
fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(x, y_integrand, label=r'$f(x) = \frac{x^2+1}{x^3+1}$', color='crimson', linestyle='--', linewidth=1.2)
ax.plot(x, y_antideriv, label=r'$F(x)$ con $C=0$', color='navy', linewidth=1.5)

ax.set_ylim(-4, 4)
ax.axhline(0, color='black', linewidth=0.8, linestyle='-')
ax.axvline(0, color='black', linewidth=0.8, linestyle='-')
ax.axvline(-1, color='gray', linewidth=0.8, linestyle=':', label='Asíntota $x=-1$')

ax.set_xlabel('$x$', fontsize=9)
ax.set_ylabel('$y$', fontsize=9)
ax.set_title('Gráfica de la función y su antiderivada', fontsize=9)
ax.legend(fontsize=7, loc='best')
ax.grid(True, linestyle=':', alpha=0.6)

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P16_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
