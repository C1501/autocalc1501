import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de la función evitando discontinuidades
x = np.linspace(-1.0, 1.0, 400)

# Antiderivada con C = 0
# F(x) = x - ln|sin(x) + cos(x)|
sin_x = np.sin(x)
cos_x = np.cos(x)
den = sin_x + cos_x

# Evitar divisiones por cero o logaritmos de números no positivos
val = np.abs(den)
F = x - np.log(val)

plt.figure(figsize=(3.5, 2.5))
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

plt.title(r'Gráfica de la Antiderivada $F(x)$', fontsize=9)
plt.xlabel(r'$x$', fontsize=8)
plt.ylabel(r'$F(x)$', fontsize=8)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=8)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()


plt.savefig(r'semana_04/graficas/SEM04_P24_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
