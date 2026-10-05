import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función original y la antiderivada con C=0
def f(x):
    return np.sqrt(x**2 + x + 1)

def F(x):
    term1 = (2*x + 1) / 4 * np.sqrt(x**2 + x + 1)
    term2 = 3 / 8 * np.log(np.abs((2 * np.sqrt(x**2 + x + 1) / np.sqrt(3)) + ((2*x + 1) / np.sqrt(3))))
    return term1 + term2

# Dominio para la gráfica
x = np.linspace(-3, 2, 400)
y_f = f(x)
y_F = F(x)

# Configuración de la figura para columna IEEE
fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(x, y_f, label=r'$f(x) = \sqrt{x^2+x+1}$', color='blue', linewidth=1.5)
ax.plot(x, y_F, label=r'$F(x)$ con $C=0$', color='red', linestyle='--', linewidth=1.5)

ax.set_title('Gráfica de la función e Integral', fontsize=9)
ax.set_xlabel('$x$', fontsize=8)
ax.set_ylabel('$y$', fontsize=8)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=7, loc='upper left')

plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()
plt.savefig(r'semana_05/graficas/SEM05_P10_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
