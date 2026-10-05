import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (3*x**2 + 3*x + 1) / (x**3 + 2*x**2 + 2*x + 1)

def F(x):
    # Antiderivada con C = 0
    return np.log(np.abs(x + 1)) + np.log(np.abs(x**2 + x + 1)) - (2 / np.sqrt(3)) * np.arctan((2*x + 1) / np.sqrt(3))

# Evitar la asíntota en x = -1 para la visualización
x1 = np.linspace(-3.5, -1.05, 400)
x2 = np.linspace(-0.95, 2.0, 400)

y1_f = f(x1)
y2_f = f(x2)

y1_F = F(x1)
y2_F = F(x2)

plt.figure(figsize=(6, 4))

# Graficar la función original f(x)
plt.plot(x1, y1_f, 'b-', label=r'$f(x)$ (Integrando)')
plt.plot(x2, y2_f, 'b-')

# Graficar la antiderivada F(x) con C = 0
plt.plot(x1, y1_F, 'r--', label=r'$F(x)$ con $C=0$ (Antiderivada)')
plt.plot(x2, y2_F, 'r--')

plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(-1, color='gray', linewidth=0.8, linestyle=':', label='Asíntota $x=-1$')

plt.title('Solución gráfica del Problema 22')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.ylim(-6, 6)
plt.legend(loc='upper left', fontsize=8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P22_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
