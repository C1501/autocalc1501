import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio para x evitando singularidades (múltiplos de pi y donde tan(x/2) = -1)
x = np.linspace(0.2, 2.5, 400)

# Antiderivada F(x) con C = 0
# F(x) = ln|tan(x/2)| + 4 / (tan(x/2) + 1)
def F(x):
    z = np.tan(x / 2.0)
    # Evitar divisiones por cero o logaritmos de cero
    with np.errstate(divide='ignore', invalid='ignore'):
        val = np.log(np.abs(z)) + 4.0 / (z + 1.0)
    return val

y = F(x)

# Configuración de la figura para formato IEEE de dos columnas
fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(x, y, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

ax.set_title(r'Gráfica de la Antiderivada', fontsize=9)
ax.set_xlabel(r'$x$', fontsize=8)
ax.set_ylabel(r'$F(x)$', fontsize=8)
ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=8)
ax.tick_params(axis='both', labelsize=7)

plt.tight_layout()

plt.savefig(r'semana_04/graficas/SEM04_P15_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
