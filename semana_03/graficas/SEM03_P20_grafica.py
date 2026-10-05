import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio para x
x = np.linspace(-3, 3, 400)

# Función integrando
def integrand(x):
    num = x**4 - x**3 - 2*x**2 - x + 2
    den = (x - 1) * (x**2 + 2)**2
    return num / den

# Antiderivada F(x) con C = 0
def antiderivative(x):
    term1 = 0.5 * np.log(x**2 + 2)
    term2 = 0.25 / (x**2 + 2)
    term3 = -x / (4 * (x**2 + 2))
    term4 = -(np.sqrt(2) / 8) * np.arctan(x / np.sqrt(2))
    return term1 + term2 + term3 + term4

y_integrand = integrand(x)
y_antideriv = antiderivative(x)

# Configuración de la gráfica para IEEE
plt.figure(figsize=(3.5, 2.5))
plt.plot(x, y_integrand, label='Integrando', color='red', linestyle='--')
plt.plot(x, y_antideriv, label=r'$F(x)$ con $C=0$', color='blue')

plt.ylim(-3, 3)
plt.axhline(0, color='black', linewidth=0.8, linestyle='-')
plt.axvline(0, color='black', linewidth=0.8, linestyle='-')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(fontsize=8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P20_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
