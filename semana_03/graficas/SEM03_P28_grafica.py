import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio evitando la asíntota x = 1 y la singularidad x = -2
x1 = np.linspace(-5, -2.1, 400)
x2 = np.linspace(-1.9, 0.9, 400)
x3 = np.linspace(1.1, 5, 400)

# Antiderivada F(x) con C = 0
def F(x):
    return (1.0/3.0) * np.log(np.abs((x + 2) / (x - 1))) - (2.0 / (x - 1))

y1 = F(x1)
y2 = F(x2)
y3 = F(x3)

plt.figure(figsize=(6, 4))
plt.plot(x1, y1, color='b', label=r'$F(x)$ con $C=0$')
plt.plot(x2, y2, color='b')
plt.plot(x3, y3, color='b')

plt.axvline(x=1, color='r', linestyle='--', label=r'Asíntota $x=1$')
plt.axvline(x=-2, color='g', linestyle=':', label=r'Asíntota $x=-2$')

plt.title('Gráfica de la Antiderivada (Problema 28)')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right', fontsize=9)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P28_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
