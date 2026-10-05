import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Parámetros para la función (ejemplo con a=1, b=4)
a = 1.0
b = 4.0

# Definimos el dominio válido para x (x >= b para evitar complejos y división por cero)
x = np.linspace(4.1, 10.0, 400)

# Antiderivada F(x) con C = 0
# F(x) = (2 / (3*(b - a))) * ((x - a)**(3/2) - (x - b)**(3/2))
F_x = (2.0 / (3.0 * (b - a))) * ((x - a)**1.5 - (x - b)**1.5)

# Configuración de la gráfica para formato de dos columnas IEEE
fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

ax.set_title(r'Gráfica de la Antiderivada ($a=1, b=4$)', fontsize=9)
ax.set_xlabel(r'$x$', fontsize=8)
ax.set_ylabel(r'$F(x)$', fontsize=8)
ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=8)

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout()

# Guardar la figura para inserción automática
plt.savefig('figura_problema_26.png', dpi=300)
plt.close()
plt.savefig(r'semana_05/graficas/SEM05_P26_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
