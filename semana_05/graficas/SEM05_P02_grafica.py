import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Generar valores para x
x = np.linspace(0.01, 1.5, 400)

# Función original y antiderivada con C = 0
# f(x) = x^(2/3) * (-1 + 2*x^(1/3))^3
f_x = (x**(2/3)) * (-1 + 2*(x**(1/3)))**3

# F(x) = -(3/5)x^(5/3) + 3x^2 - (36/7)x^(7/3) + 3x^(8/3)
F_x = - (3/5)*(x**(5/3)) + 3*(x**2) - (36/7)*(x**(7/3)) + 3*(x**(8/3))

plt.figure(figsize=(6, 4))
plt.plot(x, f_x, label=r'$f(x)$ (Integrando)', color='blue', linestyle='--')
plt.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='red')

plt.title('Gráfica de la función e Integral indefinida')
plt.xlabel('x')
plt.ylabel('Y')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left')
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P02_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
