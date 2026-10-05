import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio para la función y su antiderivada
# Se evita x = pi/2 y x = 3pi/2 donde cos(x) = 0
x = np.linspace(0.2, 1.3, 400)

# Antiderivada F(x) con C = 0
# F(x) = ln( (1 + cos(x))^2 / cos(x) )
F = np.log((1 + np.cos(x))**2 / np.cos(x))

# Configuración de la figura para columna IEEE
fig, ax = plt.subplots(figsize=(3.5, 2.5))

# Graficar la curva con la etiqueta obligatoria para C = 0
ax.plot(x, F, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

# Etiquetas y formato
ax.set_title(r'Gráfica de la Antiderivada', fontsize=9)
ax.set_xlabel(r'$x$', fontsize=8)
ax.set_ylabel(r'$F(x)$', fontsize=8)
ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
ax.legend(fontsize=8)
ax.grid(True, linestyle=':', alpha=0.6)

# Ajustes de bordes
plt.tight_layout()

plt.savefig(r'semana_04/graficas/SEM04_P22_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
