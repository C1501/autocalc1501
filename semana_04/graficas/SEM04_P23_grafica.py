import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio para x
x = np.linspace(0, 2.5, 400)

# Antiderivada F(x) con C = 0
# F(x) = -0.5*cos(x)**2 - 3*cos(x) - 8*ln(|3 - cos(x)|)
F_x = -0.5 * np.cos(x)**2 - 3 * np.cos(x) - 8 * np.log(np.abs(3 - np.cos(x)))

plt.figure(figsize=(6, 4))
plt.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='b', linewidth=2)
plt.title(r'Gráfica de la antiderivada $F(x)$')
plt.xlabel(r'$x$')
plt.ylabel(r'$F(x)$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='best')
plt.tight_layout()

plt.savefig(r'semana_04/graficas/SEM04_P23_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
