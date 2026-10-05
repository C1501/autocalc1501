import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de la función
x = np.linspace(-3, 3, 400)

# Definir la función integrando f(x)
f_x = 1.0 / np.sqrt(x**2 + x + 1)

# Definir la antiderivada F(x) con C = 0
F_x = np.log(np.abs(x + 0.5 + np.sqrt(x**2 + x + 1)))

# Configuración de la figura para columna IEEE
fig, ax = plt.subplots(figsize=(3.5, 2.5))

# Graficar las curvas
ax.plot(x, f_x, 'b-', label=r'$f(x)$')
ax.plot(x, F_x, 'r--', label=r'$F(x)$ con $C=0$')

# Configuración de ejes y leyenda
ax.set_xlim([-3, 3])
ax.set_ylim([-2, 3])
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
ax.set_xlabel(r'$x$', fontsize=9)
ax.set_ylabel(r'$y$', fontsize=9)
ax.legend(fontsize=8, loc='upper left')
ax.grid(True, linestyle=':', alpha=0.6)

# Ajustar diseño
plt.tight_layout()

# Guardar la figura
plt.savefig('SEM05_P08_grafica.pdf', dpi=300)
plt.close()
plt.savefig(r'semana_05/graficas/SEM05_P08_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
