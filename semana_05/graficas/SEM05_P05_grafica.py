import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio de la función (x > 1 para evitar división por cero y log negativo)
x = np.linspace(1.05, 5.0, 400)

# Antiderivada F(x) con C = 0
# F(x) = (2/3)*x**(3/2) + x + 2*sqrt(x) + 2*ln|sqrt(x) - 1|
F = (2.0/3.0) * x**(1.5) + x + 2.0 * np.sqrt(x) + 2.0 * np.log(np.abs(np.sqrt(x) - 1.0))

plt.figure(figsize=(6, 4))
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='b', linewidth=2)

plt.title('Gráfica de la Antiderivada', fontsize=10)
plt.xlabel('$x$', fontsize=9)
plt.ylabel('$F(x)$', fontsize=9)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=9)
plt.tight_layout()


plt.savefig(r'semana_05/graficas/SEM05_P05_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
