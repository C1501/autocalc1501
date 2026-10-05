import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio para x donde el radical es real (4x^2 + 4x - 3 > 0)
# Las raíces de 4x^2 + 4x - 3 = (2x-1)(2x+3) son x = 0.5 y x = -1.5
# El dominio es x < -1.5 o x > 0.5. Graficaremos la rama derecha (x > 0.5)
x = np.linspace(0.51, 3.0, 400)

# Función integrando f(x)
f = 1.0 / np.sqrt(4*x**2 + 4*x - 3)

# Antiderivada F(x) con C = 0
F = 0.5 * np.log(np.abs(2*x + 1 + np.sqrt(4*x**2 + 4*x - 3)))

plt.figure(figsize=(6, 3.5))
plt.plot(x, f, label=r'$f(x)$ (Integrando)', color='blue', linewidth=1.5)
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='red', linestyle='--', linewidth=1.5)

plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.title('Gráfica de la función y su antiderivada (SEM05_P07)', fontsize=10)
plt.xlabel('$x$', fontsize=9)
plt.ylabel('$y$', fontsize=9)
plt.legend(fontsize=8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.xlim(0.5, 3.0)
plt.ylim(-0.5, 2.5)
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P07_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
