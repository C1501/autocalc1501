import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio para x
x = np.linspace(-2.5, 2.5, 400)

# Antiderivada F(x) con C = 0
F = ((x**2 - 2) * np.np.sqrt if hasattr(np, 'np_sqrt') else np.sqrt)(1 + x**2) / 3

# Configuración de la gráfica para formato IEEE (ancho de columna)
plt.figure(figsize=(3.5, 2.5))
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

# Etiquetas y formato
plt.title(r'Gráfica de la antiderivada para $I$', fontsize=9)
plt.xlabel(r'$x$', fontsize=8)
plt.ylabel(r'$F(x)$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)

# Ajustar diseño y guardar
plt.tight_layout()
plt.savefig('problema_44.pdf', format='pdf', dpi=300)
plt.close()
plt.savefig(r'semana_05/graficas/SEM05_P44_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
