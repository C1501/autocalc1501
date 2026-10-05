import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio evitando la asíntota en x = 2
x1 = np.linspace(-3, 1.9, 400)
x2 = np.linspace(2.1, 5, 400)

# Antiderivada F(x) con C = 0
def F(x):
    return (1/5) * np.log(x**2 + 1) + (4/5) * np.arctan(x) + (3/5) * np.log(np.abs(x - 2))

y1 = F(x1)
y2 = F(x2)

plt.figure(figsize=(6, 4))
plt.plot(x1, y1, 'b-', label=r'$F(x)$ con $C=0$')
plt.plot(x2, y2, 'b-')
plt.axvline(x=2, color='r', linestyle='--', label=r'Asintota $x=2$')

plt.title('Gráfica de la Antiderivada (Problema 18)')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.ylim(-4, 4)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='lower right')
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P18_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
