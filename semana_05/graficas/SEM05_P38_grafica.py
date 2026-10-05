import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio seguro para evitar división por cero y raíces negativas
x = np.linspace(0.01, 1.99, 400)

# Antiderivada F(x) con C = 0
# F(x) = - (4 - x^4)^(1/4) / (2x)
F_x = -((4 - x**4)**0.25) / (2 * x)

plt.figure(figsize=(3.5, 2.5))
plt.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

plt.title(r'Gráfica de la antiderivada (Prob 38)', fontsize=9)
plt.xlabel(r'$x$', fontsize=8)
plt.ylabel(r'$F(x)$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P38_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
