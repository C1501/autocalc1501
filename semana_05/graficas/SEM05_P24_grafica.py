import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del rango de x (evitando x = 0 por la asíntota)
x1 = np.linspace(-3, -0.05, 400)
x2 = np.linspace(0.05, 3, 400)

# Antiderivada con C = 0
def F(x):
    return np.log(np.abs((np.sqrt(x**2 + 1) - 1) / x))

y1 = F(x1)
y2 = F(x2)

plt.figure(figsize=(6, 4))
plt.plot(x1, y1, 'b-', label=r'$F(x)$ con $C=0$')
plt.plot(x2, y2, 'b-')

plt.title('Gráfica de la antiderivada (Problema 24)')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.ylim(-3, 3)
plt.legend(loc='upper right')
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P24_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
