import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de la función, evitando valores donde x^3 + 9 <= 0
x = np.linspace(-2.0, 5.0, 400)

# Función original y antiderivada con C = 0
# I = 4*(x**3 + 36) / (9 * (9 + x**3)**0.25)
def F(x):
    return (4.0 * (x**3 + 36.0)) / (9.0 * (9.0 + x**3)**0.25)

y = F(x)

plt.figure(figsize=(4, 3))
plt.plot(x, y, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)
plt.title('Antiderivada del Problema 37')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='best')
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P37_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
