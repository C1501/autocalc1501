import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio para x evitando las asíntotas y singularidades
x = np.linspace(-1.2, 1.2, 400)

# Antiderivada F(x) con C = 0
def F(x):
    z = np.tan(x / 2.0)
    num = 2 * z + 3 - np.sqrt(13)
    den = 2 * z + 3 + np.sqrt(13)
    # Evitar divisiones por cero o logaritmos negativos
    val = np.abs(num / den)
    return - (1.0 / np.sqrt(13)) * np.log(val)

y = F(x)

# Configuración de la gráfica para formato IEEE de dos columnas
fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(x, y, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

ax.set_title(r'Gráfica de la Antiderivada', fontsize=9)
ax.set_xlabel(r'$x$', fontsize=8)
ax.set_ylabel(r'$F(x)$', fontsize=8)
ax.tick_params(axis='both', which='major', labelsize=7)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(fontsize=7, loc='best')

plt.tight_of_layout = True
plt.savefig('grafica_problema_28.png', dpi=300, bbox_inches='tight')
plt.close()
plt.savefig(r'semana_04/graficas/SEM04_P28_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
