import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio para la función original y su antiderivada
# La función original f(x) = 1 / (x * sqrt(1 + x - x^2)) requiere 1 + x - x^2 > 0 y x != 0
# Raíces de 1 + x - x^2 = 0 son x = (1 +- sqrt(5)) / 2
# Aprox: x1 = -0.618, x2 = 1.618. 
# Tomamos el intervalo positivo donde x > 0, es decir, de 0 a (1 + sqrt(5))/2 ≈ 1.618

x = np.linspace(0.2, 1.55, 400)

# Función original
f = 1.0 / (x * np.sqrt(1.0 + x - x**2))

# Antiderivada con C = 0
# F(x) = -ln | 1/x + 0.5 + sqrt(1/x^2 + 1/x - 1) |
u = 1.0 / x
F = -np.log(np.abs(u + 0.5 + np.sqrt(u**2 + u - 1.0)))

plt.figure(figsize=(6, 4))
plt.plot(x, f, label=r'$f(x)$', color='blue', linewidth=1.5)
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='red', linestyle='--', linewidth=1.5)

plt.title('Gráfica de la función y su antiderivada')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.ylim(-4, 4)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='best')
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P49_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
