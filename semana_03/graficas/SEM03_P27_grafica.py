import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio para x, evitando la asíntota en x = 1
x1 = np.linspace(-3, 0.95, 400)
x2 = np.linspace(1.05, 4, 400)

# Función integranda f(x)
def f(x):
    return (3*x**2 + x - 2) / ((x - 1)*(x**2 + 1))

# Antiderivada F(x) con C = 0
def F(x):
    return np.log(np.abs(x - 1)) + np.log(x**2 + 1) + 3 * np.arctan(x)

y1_f = f(x1)
y2_f = f(x2)
y1_F = F(x1)
y2_F = F(x2)

plt.figure(figsize=(6, 4))

# Graficar la función integranda
plt.plot(x1, y1_f, 'b-', label=r'$f(x)$ (Integrando)')
plt.plot(x2, y2_f, 'b-')

# Graficar la antiderivada especificando C = 0 en la etiqueta
plt.plot(x1, y1_F, 'r--', label=r'$F(x)$ con $C=0$')
plt.plot(x2, y2_F, 'r--')

plt.axvline(x=1, color='gray', linestyle=':', alpha=0.7, label=r'Asíntota $x=1$')

plt.title('Gráfica del Integrando y su Antiderivada')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.ylim(-10, 15)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend(loc='upper left', fontsize=9)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P27_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
