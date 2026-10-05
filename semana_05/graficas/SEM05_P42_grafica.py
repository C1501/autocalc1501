import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de x (valores positivos debido a las potencias fraccionarias)
x = np.linspace(0.01, 1.5, 400)

# Definir la función integrando f(x)
def integrand(x):
    return (x**(3/2)) * ((2 * (x**(1/3)) - 1)**3)

# Definir la antiderivada F(x) con C = 0
def antiderivative(x):
    term1 = (16/7) * (x**(7/2))
    term2 = (72/19) * (x**(19/6))
    term3 = (36/17) * (x**(17/6))
    term4 = (2/5) * (x**(5/2))
    return term1 - term2 + term3 - term4

y_integrand = integrand(x)
y_antideriv = antiderivative(x)

# Configuración de la gráfica para formato IEEE
plt.figure(figsize=(6, 3.5))
plt.plot(x, y_integrand, label=r'$f(x) = x^{3/2}(2x^{1/3}-1)^3$', color='blue', linestyle='--')
plt.plot(x, y_antideriv, label=r'$F(x)$ con $C=0$', color='red')

plt.title('Gráfica del Integrando y su Antiderivada (Problema 42)')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='best', fontsize=9)
plt.tight_layout()


plt.savefig(r'semana_05/graficas/SEM05_P42_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
