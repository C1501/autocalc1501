import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de x evitando las asíntotas en x = -1 y x = 1
x1 = np.linspace(-3, -1.1, 400)
x2 = np.linspace(-0.9, 0.9, 400)
x3 = np.linspace(1.1, 3, 400)

# Antiderivada F(x) con C = 0
def F(x):
    return (x**4)/4 + (x**2)/2 + (1.5)*np.log(np.abs(x-1)) - (0.5)*np.log(np.abs(x+1))

y1 = F(x1)
y2 = F(x2)
y3 = F(x3)

plt.figure(figsize=(6, 4))
plt.plot(x1, y1, 'b-', label=r'$F(x)$ con $C=0$')
plt.plot(x2, y2, 'b-')
plt.plot(x3, y3, 'b-')

plt.axvline(x=-1, color='r', linestyle='--', alpha=0.6, label='Asíntotas')
plt.axvline(x=1, color='r', linestyle='--', alpha=0.6)

plt.title('Gráfica de la antiderivada $F(x)$')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.ylim(-10, 15)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', fontsize=9)
plt.tight_layout()
plt.savefig(r'semana_03/graficas/SEM03_P14_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
