import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores para x (evitando discontinuidades y raíces complejas con partes reales negativas)
x = np.linspace(0.5, 5.0, 400)

# Antiderivada F(x) con C = 0
# F(x) = x^2 / 2 + ln(x) - 0.5 * ln(x^2 - 2x + 3)
F = (x**2) / 2.0 + np.log(np.abs(x)) - 0.5 * np.log(np.abs(x**2 - 2.0*x + 3.0))

plt.figure(figsize=(6, 4))
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='b', linewidth=2)
plt.title('Gráfica de la antiderivada (Problema 13)')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P13_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
