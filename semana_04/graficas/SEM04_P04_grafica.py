import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio para x, evitando las asíntotas en x = pi + 2k*pi
x = np.linspace(-2.5, 2.5, 400)

# Función original f(x) = 1 / (1 + cos(x))
# Función antiderivada F(x) con C = 0 -> F(x) = tan(x/2)
f_x = 1.0 / (1.0 + np.cos(x))
F_x = np.tan(x / 2.0)

# Configuración de la figura para columna IEEE
fig, ax = plt.subplots(figsize=(3.5, 2.5))

# Graficar ambas funciones
ax.plot(x, f_x, label=r'$f(x) = \frac{1}{1+\cos x}$', color='tab:blue')
ax.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='tab:orange', linestyle='--')

# Configuración de ejes y límites
ax.set_ylim(-5, 5)
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
ax.set_xlabel('$x$', fontsize=9)
ax.set_ylabel('$y$', fontsize=9)
ax.legend(loc='upper center', fontsize=8)
ax.grid(True, linestyle=':', alpha=0.6)

# Ajustar diseño
plt.tight_layout()
plt.savefig(r'semana_04/graficas/SEM04_P04_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
