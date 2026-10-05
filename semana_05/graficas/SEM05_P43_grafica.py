import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio para x, evitando los puntos donde la función no está definida (|x| >= 1)
x = np.linspace(-0.95, 0.95, 400)

# Definir la antiderivada F(x) con C = 0
F_x = (2 - x**2) / np.sqrt(1 - x**2)

plt.figure(figsize=(6, 4))
plt.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='b', linewidth=2)

plt.title(r'Gráfica de la antiderivada $F(x)$ para el Problema 43')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.8, linestyle='-')
plt.axvline(0, color='black', linewidth=0.8, linestyle='-')
plt.legend(loc='upper center')
plt.ylim(-1, 10)

plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P43_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
