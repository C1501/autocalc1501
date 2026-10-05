import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio para evitar discontinuidades de la función
x = np.linspace(-1.2, 1.2, 400)

# Antiderivada F(x) con C = 0
# F(x) = -0.5 * ln(|cos(x)|) + 0.5 / (1 + sin(x))
F = -0.5 * np.log(np.abs(np.cos(x))) + 0.5 / (1.0 + np.sin(x))

plt.figure(figsize=(6, 4))
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='b', linewidth=2)
plt.title('Gráfica de la Antiderivada')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(-2, 4)
plt.legend()
plt.tight_layout()

plt.savefig(r'semana_04/graficas/SEM04_P08_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
