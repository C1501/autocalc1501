import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición de parámetros para graficar (a=1, b=1)
a = 1.0
b = 1.0

# Definición del dominio para x (evitando valores donde la base sea negativa)
x = np.linspace(0.0, 2.0, 400)

# Antiderivada F(x) con C = 0
# F(x) = (4/(27*b^2)) * (a + b*x^3)^(9/4) - (4*a/(15*b^2)) * (a + b*x^3)^(5/4)
term1 = (4.0 / (27.0 * b**2)) * (a + b * x**3)**(9.0 / 4.0)
term2 = (4.0 * a / (15.0 * b**2)) * (a + b * x**3)**(5.0 / 4.0)
F_x = term1 - term2

# Configuración de la figura para IEEE (ancho de columna)
fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

ax.set_title(r'Antiderivada $I = \int x^3(1+x^3)^{1/4}dx$', fontsize=9)
ax.set_xlabel('$x$', fontsize=8)
ax.set_ylabel('$F(x)$', fontsize=8)
ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=8)
ax.tick_params(axis='both', which='major', labelsize=8)

plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P28_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
