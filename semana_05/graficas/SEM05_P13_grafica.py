import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio para x donde la función y la antiderivada son reales
# 1 + x - x^2 > 0 -> raices en (1 - sqrt(5))/2approx -0.618 y (1 + sqrt(5))/2 approx 1.618
x_min = (-1 + np.sqrt(5)) / 2 + 0.01  # Evitar división por cero y raíces negativas
x_max = (1 + np.sqrt(5)) / 2 - 0.01

x = np.linspace(x_min, x_max, 400)

# Función integrando f(x)
f_x = 1 / (x * np.sqrt(1 + x - x**2))

# Antiderivada F(x) con C = 0
# F(x) = -ln | 1/x + 1/2 + sqrt(1/x^2 + 1/x - 1) |
term_inside = 1/x + 0.5 + np.sqrt(1/(x**2) + 1/x - 1)
F_x = -np.log(np.abs(term_inside))

plt.figure(figsize=(6, 4))
plt.plot(x, f_x, label=r'$f(x)$', color='blue', linestyle='--')
plt.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='red')

plt.title('Gráfica de la función y su antiderivada')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlim(x_min, x_max)
plt.ylim(-4, 4)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='best')
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P13_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
