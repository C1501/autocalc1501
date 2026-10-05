import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio evitando las asíntotas en x = -1 y x = 3
x1 = np.linspace(-3.5, -1.1, 400)
x2 = np.linspace(-0.9, 2.9, 400)
x3 = np.linspace(3.1, 6.0, 400)

# Antiderivada F(x) con C = 0
def F(x):
    return (x**2)/2.0 + 2.0*x + (27.0/4.0)*np.log(np.abs(x - 3.0)) + (1.0/4.0)*np.log(np.abs(x + 1.0))

y1 = F(x1)
y2 = F(x2)
y3 = F(x3)

plt.figure(figsize=(3.5, 2.8))

plt.plot(x1, y1, 'b-', label=r'$F(x)$ con $C=0$')
plt.plot(x2, y2, 'b-')
plt.plot(x3, y3, 'b-')

# Líneas verticales para las asíntotas
plt.axvline(x=-1, color='r', linestyle='--', alpha=0.6, label='Asíntotas')
plt.axvline(x=3, color='r', linestyle='--', alpha=0.6)

plt.title('Antiderivada del Problema 15', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$F(x)$', fontsize=8)
plt.ylim(-15, 25)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=7, loc='upper left')

plt.tight_layout()
plt.savefig(r'semana_03/graficas/SEM03_P15_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
