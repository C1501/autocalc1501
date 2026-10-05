import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función y su antiderivada (con C=0)
def f(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        val = np.sqrt(x) / (x - 1)
        val[x == 1] = np.nan
        return val

def F(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        val = 2 * np.sqrt(x) + np.log(np.abs((np.sqrt(x) - 1) / (np.sqrt(x) + 1)))
        val[x == 1] = np.nan
        return val

# Generar puntos para la gráfica (evitando x=1 y x<0)
x1 = np.linspace(0.001, 0.99, 400)
x2 = np.linspace(1.01, 6.0, 400)

y1_f = f(x1)
y2_f = f(x2)
y1_F = F(x1)
y2_F = F(x2)

# Configuración de la figura para IEEE (ancho de columna)
fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(x1, y1_f, color='tab:blue', linestyle='--', label=r'$f(x)$')
ax.plot(x2, y2_f, color='tab:blue', linestyle='--')

ax.plot(x1, y1_F, color='tab:orange', linestyle='-', label=r'$F(x)$ con $C=0$')
ax.plot(x2, y2_F, color='tab:orange', linestyle='-')

ax.set_xlim(0, 6)
ax.set_ylim(-6, 8)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(1, color='gray', linewidth=0.5, linestyle=':')
ax.set_xlabel('$x$', fontsize=9)
ax.set_ylabel('$y$', fontsize=9)
ax.legend(fontsize=8, loc='lower right')
ax.grid(True, linestyle=':', alpha=0.6)

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P06_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
