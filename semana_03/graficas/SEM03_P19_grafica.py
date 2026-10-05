import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (3*x**2 + 2*x - 2) / (x**3 - 1)

def F(x):
    # Antiderivada con C = 0
    return np.log(np.abs(x**3 - 1)) + (4 / np.sqrt(3)) * np.arctan((2*x + 1) / np.sqrt(3))

# Evitamos la asíntota en x = 1
x1 = np.linspace(-2, 0.95, 400)
x2 = np.linspace(1.05, 4, 400)

y1_f = f(x1)
y2_f = f(x2)
y1_F = F(x1)
y2_F = F(x2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.2))

# Gráfica de la función original
ax1.plot(x1, y1_f, 'b-', label=r'$f(x)$')
ax1.plot(x2, y2_f, 'b-')
ax1.axvline(x=1, color='red', linestyle='--', alpha=0.6, label='Asintota $x=1$')
ax1.set_title('Funcion Integrando')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$f(x)$')
ax1.set_ylim(-10, 10)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(fontsize=8)

# Gráfica de la antiderivada
ax2.plot(x1, y1_F, 'g-', label=r'$F(x)$ con $C=0$')
ax2.plot(x2, y2_F, 'g-')
ax2.axvline(x=1, color='red', linestyle='--', alpha=0.6, label='Asintota $x=1$')
ax2.set_title('Antiderivada')
ax2.set_xlabel('$x$')
ax2.set_ylabel('$F(x)$')
ax2.set_ylim(-10, 10)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(fontsize=8)

plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P19_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
