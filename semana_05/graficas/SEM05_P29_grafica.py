import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio para la función y su antiderivada
# Evitamos x = -1 para prevenir divisiones por cero en (-1)^(3/2)
x = np.linspace(-0.9, 4.0, 400)

# Antiderivada F(x) con C = 0
def F(x):
    return x / np.sqrt(1.0 + x**3)

y = F(x)

# Configuración de la figura para formato IEEE de dos columnas
fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(x, y, 'b-', label=r'$F(x)$ con $C=0$')

ax.set_title(r'Gráfica de la solución $F(x)$', fontsize=9)
ax.set_xlabel('$x$', fontsize=8)
ax.set_ylabel('$F(x)$', fontsize=8)
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
ax.grid(True, linestyle=':', alpha=0.6)
ax.tick_params(axis='both', labelsize=7)
ax.legend(fontsize=7)

plt.tight_confinement = True
plt.savefig('resultado_29.png', dpi=300, bbox_inches='tight')
plt.savefig(r'semana_05/graficas/SEM05_P29_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
