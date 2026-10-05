import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio para x > 0
x = np.linspace(0.01, 6.0, 400)

# Antiderivada con C = 0
# F(x) = -2*sqrt(x) + 4*x^(1/4) - 4*ln(1 + x^(1/4))
def F(x_val):
    term1 = -2 * np.sqrt(x_val)
    term2 = 4 * (x_val ** 0.25)
    term3 = -4 * np.log(1 + (x_val ** 0.25))
    return term1 + term2 + term3

y = F(x)

# Configuración de la gráfica para formato IEEE de dos columnas
fig, ax = plt.subplots(figsize=(3.5, 2.5), dpi=300)

ax.plot(x, y, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

ax.set_title(r'Gráfica de la antiderivada $F(x)$', fontsize=9)
ax.set_xlabel(r'$x$', fontsize=8)
ax.set_ylabel(r'$F(x)$', fontsize=8)
ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
ax.axvline(0, color='black', linewidth=0.5, linestyle='--')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=8)
ax.tick_params(axis='both', labelsize=7)

plt.tight_layout()
plt.savefig('SEM05_P41_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
plt.savefig(r'semana_05/graficas/SEM05_P41_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
