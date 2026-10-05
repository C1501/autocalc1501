import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio para x que hace que el argumento de la raíz sea positivo
# -9x^2 + 3x + 4 > 0 -> Raíces en x = (1 - sqrt(17))/6 y (1 + sqrt(17))/6
x_min = (1 - np.sqrt(17)) / 6 + 0.01
x_max = (1 + np.sqrt(17)) / 6 - 0.01

x = np.linspace(x_min, x_max, 400)
# Antiderivada con C = 0
y = (2.0 / 3.0) * np.arcsin((6.0 * x - 1.0) / (2.0 * np.sqrt(17)))

plt.figure(figsize=(6, 3.5))
plt.plot(x, y, label=r'$F(x)$ con $C=0$', color='b', linewidth=2)
plt.title('Antiderivada del Problema 22')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='best')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P22_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
