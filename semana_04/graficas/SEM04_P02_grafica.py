import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.2, 1.2, 400)
# F(x) con C = 0 -> F(x) = x - tan(x) + sec(x)
# Evitamos discontinuidades extremas de sec(x) y tan(x) en el rango graficado
y = x - np.tan(x) + 1.0 / np.cos(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y, label=r'$F(x)$ con $C=0$', color='b', linewidth=2)
plt.title('Antiderivada del Problema 02')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(-5, 5)
plt.legend()
plt.axhline(0, color='black', linewidth=0.8, linestyle='-')
plt.axvline(0, color='black', linewidth=0.8, linestyle='-')
plt.tight_layout()

plt.savefig(r'semana_04/graficas/SEM04_P02_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
