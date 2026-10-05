import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de la función (fuera del intervalo donde el radical es imaginario)
# 4x^2 + 4x - 3 > 0 => (2x-1)(2x+3) > 0 => x < -1.5 o x > 0.5
x1 = np.linspace(-3.0, -1.501, 400)
x2 = np.linspace(0.501, 3.0, 400)

# Función original f(x)
def f(x):
    return 1.0 / np.sqrt(4*x**2 + 4*x - 3)

# Antiderivada F(x) con C = 0
def F(x):
    return 0.5 * np.log(np.abs(2*x + 1 + np.sqrt(4*x**2 + 4*x - 3)))

plt.figure(figsize=(6, 4))

# Graficar para x < -1.5
plt.plot(x1, f(x1), color='blue', linestyle='--', label=r'$f(x)$')
plt.plot(x1, F(x1), color='red', label=r'$F(x)$ con $C=0$')

# Graficar para x > 0.5
plt.plot(x2, f(x2), color='blue', linestyle='--')
plt.plot(x2, F(x2), color='red')

plt.axvline(x=-1.5, color='gray', linestyle=':', alpha=0.7)
plt.axvline(x=0.5, color='gray', linestyle=':', alpha=0.7)

plt.title('Gráfica de $f(x)$ y su Antiderivada $F(x)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.ylim(-3, 3)
plt.axhline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P46_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
