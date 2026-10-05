import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0, 2.5, 400)
# F(x) con C = 0 para la antiderivada: F(x) = -ln(1 + cos(x))
# Evitamos la asíntota en x = pi (~3.14), por lo que graficamos en un dominio seguro
y_integral = -np.log(np.abs(1 + np.cos(x)))

plt.figure(figsize=(3.5, 2.5))
plt.plot(x, y_integral, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

plt.title('Antiderivada de $\\frac{\\sin x}{1 + \\cos x}$', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$F(x)$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()
plt.savefig(r'semana_04/graficas/SEM04_P06_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
