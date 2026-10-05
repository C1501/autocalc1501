import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de la función
x = np.linspace(-2, 2, 400)

# Definir la antiderivada F(x) con C = 0
F = (3/10) * (1 + x**2)**(5/3) - (3/4) * (1 + x**2)**(2/3)

# Configuración de la gráfica para formato IEEE de dos columnas
fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(x, F, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

ax.set_title('Gráfica de la Antiderivada', fontsize=9)
ax.set_xlabel('$x$', fontsize=8)
ax.set_ylabel('$F(x)$', fontsize=8)
ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
ax.axvline(0, color='black', linewidth=0.5, linestyle='--')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=8)
ax.tick_params(axis='both', labelsize=8)

plt.tight_layout()
plt.savefig('grafica_integral.png', dpi=300)
plt.close()
plt.savefig(r'semana_05/graficas/SEM05_P32_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
