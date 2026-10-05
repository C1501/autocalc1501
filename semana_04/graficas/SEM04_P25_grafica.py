import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Configuración de estilo para IEEE de dos columnas
plt.rcParams.update({
    'font.size': 8,
    'axes.labelsize': 8,
    'legend.fontsize': 7,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'figure.figsize': (3.5, 2.5),
    'figure.autolayout': True
})

# Definir el dominio evitando las asíntotas de la tangente y secante
x = np.linspace(-1.2, 1.2, 400)

# Función original (integrando) y la antiderivada con C=0
integrand = 1.0 / (4.0 * np.sin(x)**2 + 9.0 * np.cos(x)**2)
F_x = (1.0 / 6.0) * np.arctan((2.0 * np.tan(x)) / 3.0)

fig, ax = plt.subplots()

ax.plot(x, integrand, label=r'Integrando $f(x)$', color='tab:red', linestyle='--')
ax.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='tab:blue', linewidth=1.5)

ax.set_title(r'Gráfica de $f(x)$ y su Antiderivada $F(x)$', fontsize=8)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.axhline(0, color='black', linewidth=0.5, linestyle='-')
ax.axvline(0, color='black', linewidth=0.5, linestyle='-')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper left')


plt.savefig(r'semana_04/graficas/SEM04_P25_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
