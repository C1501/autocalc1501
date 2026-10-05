import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Generar valores de x en el dominio (-1, 1) para evitar divisiones por cero y raíces negativas
x = np.linspace(-0.99, 0.99, 400)

# Calcular la función F(x) con C = 0
# F(x) = 1/sqrt(1 - x^2) + sqrt(1 - x^2)
F = (1.0 / np.sqrt(1.0 - x**2)) + np.sqrt(1.0 - x**2)

plt.figure(figsize=(6, 4))
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='b', linewidth=2)

plt.title('Gráfica de la Antiderivada (Problema 03)')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.8, linestyle='-')
plt.axvline(0, color='black', linewidth=0.8, linestyle='-')
plt.ylim(0, 6)
plt.legend(loc='upper center')
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P03_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
