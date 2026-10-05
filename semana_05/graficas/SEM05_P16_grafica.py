import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio de la función (evitando valores donde el denominador sea complejo)
x = np.linspace(0.8, 5.0, 400)

# Definición de la antiderivada F(x) con C = 0
def F(x):
    termino_algebraico = (x**2 + (1/3)*x - (1/3)) * np.sqrt(3*x**2 - 2*x + 1)
    termino_logaritmico = (4 / (3 * np.sqrt(3))) * np.log(np.abs(x - (1/3) + np.sqrt(x**2 - (2/3)*x + (1/3))))
    return termino_algebraico + termino_logaritmico

y = F(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y, label=r'$F(x)$ con $C=0$', color='blue', linewidth=2)
plt.title('Antiderivada del Problema 16')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P16_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
