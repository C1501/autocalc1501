import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio para x > 0
x = np.linspace(0.05, 3.0, 400)

# Función auxiliar y logaritmo
f_x = x - np.log(x)
ln_x = np.log(x)

plt.figure(figsize=(6, 4))

# Curvas principales
plt.plot(x, ln_x, label=r'$\ln(x)$', color='blue', linewidth=1.5)
plt.plot(x, x, label=r'$y = x$', color='red', linestyle='--', linewidth=1.5)
plt.plot(x, f_x, label=r'$F(x)$ con $C=0$', color='green', linewidth=1.5)

# Configuración del gráfico
plt.title(r'Comportamiento de $\ln(x)$ vs $x$', fontsize=10)
plt.xlabel(r'$x$', fontsize=9)
plt.ylabel(r'$y$', fontsize=9)
plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.axvline(0, color='black', linewidth=0.8, linestyle=':')
plt.xlim(0, 3)
plt.ylim(-3, 3)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=8, loc='upper left')

plt.tight_layout()

# Se guarda ÚNICAMENTE en la carpeta objetivo antes de cerrar la figura
plt.savefig(r'semana_08/graficas/SEM08_P02_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
