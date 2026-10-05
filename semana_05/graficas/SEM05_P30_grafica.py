import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio para x (evitando x = 0)
x = np.linspace(0.2, 4.0, 400)

# Antiderivada F(x) con C = 0
# F(x) = -sqrt(x^2 + 1) / (2*x^2) - 0.5 * ln((sqrt(x^2 + 1) + 1) / x)
def F(x_val):
    term1 = -np.sqrt(x_val**2 + 1) / (2 * x_val**2)
    term2 = -0.5 * np.log((np.sqrt(x_val**2 + 1) + 1) / x_val)
    return term1 + term2

y = F(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y, label=r'$F(x)$ con $C=0$', color='b', linewidth=2)
plt.title('Gráfica de la Antiderivada (Problema 30)')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P30_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
