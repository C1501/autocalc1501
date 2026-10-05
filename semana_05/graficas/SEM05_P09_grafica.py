import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir la función y su antiderivada (con C = 0)
def f(x):
    return np.sqrt(x**2 + x + 1)

def F(x):
    term1 = ((2*x + 1) / 4) * np.sqrt(x**2 + x + 1)
    term2 = (3 / 8) * np.log(np.abs((2 * np.sqrt(x**2 + x + 1) + 2*x + 1) / np.sqrt(3)))
    return term1 + term2

# Rango de valores para x
x = np.linspace(-3, 2, 400)
y_integrando = f(x)
y_antiderivada = F(x)

# Configuración de la gráfica para formato IEEE (ancho de una columna)
plt.figure(figsize=(3.5, 2.5))

plt.plot(x, y_integrando, 'b-', label=r'$f(x) = \sqrt{x^2+x+1}$')
plt.plot(x, y_antiderivada, 'r--', label=r'$F(x)$ con $C=0$')

plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')

plt.title(r'Gráfica para el Problema 09', fontsize=9)
plt.xlabel(r'$x$', fontsize=8)
plt.ylabel(r'$y$', fontsize=8)
plt.legend(fontsize=7, loc='upper center')
plt.grid(True, linestyle=':', alpha=0.6)

plt.xticks(fontsize=7)
plt.yticks(fontsize=7)

plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P09_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
