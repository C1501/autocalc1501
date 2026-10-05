import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio evitando la asíntota en x = 2
x1 = np.linspace(-1.5, 1.95, 400)
x2 = np.linspace(2.05, 5.5, 400)

# Antiderivada F(x) con C = 0
def F(x):
    return (x**2) / 2.0 - 3.0 / ((x - 2)**2)

y1 = F(x1)
y2 = F(x2)

plt.figure(figsize=(3.5, 2.5))
plt.plot(x1, y1, 'b-', label=r'$F(x)$ con $C=0$')
plt.plot(x2, y2, 'b-')
plt.axvline(x=2, color='r', linestyle='--', label=r'Asíntota $x=2$')

plt.title('Gráfica de la Antiderivada', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$F(x)$', fontsize=8)
plt.ylim(-20, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=7, loc='lower right')
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()
plt.savefig(r'semana_03/graficas/SEM03_P09_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
