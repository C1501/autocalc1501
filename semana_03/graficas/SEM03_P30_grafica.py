import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de la función, evitando la asíntota vertical en x = 1/3 ≈ 0.333
x1 = np.linspace(-2, 0.3, 400)
x2 = np.linspace(0.36, 3, 400)

def antiderivada(x):
    # F(x) con C = 0
    term1 = (5/11) * np.log(np.abs(3*x - 1))
    term2 = -(5/22) * np.log(x**2 + x/3 + 1)
    term3 = (9 / (2 * np.sqrt(35))) * np.arctan((6*x + 1) / np.sqrt(35))
    return term1 + term2 + term3

y1 = antiderivada(x1)
y2 = antiderivada(x2)

plt.figure(figsize=(6, 4))
plt.plot(x1, y1, label=r'$F(x)$ con $C=0$', color='b')
plt.plot(x2, y2, color='b')

plt.axvline(x=1/3, color='r', linestyle='--', label=r'Asíntota $x = 1/3$')
plt.title('Gráfica de la Antiderivada $F(x)$')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.ylim(-5, 5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='upper left')
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P30_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
