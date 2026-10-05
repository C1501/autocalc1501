import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**(-1) * (4 + 3*x**4)**(1.5)

def F(x):
    z = np.sqrt(4 + 3*x**4)
    term1 = (z**3) / 6
    term2 = 2 * z
    term3 = np.log(np.abs((z - 2) / (z + 2)))
    return term1 + term2 + term3

x = np.linspace(0.5, 2.0, 400)
y_vals = F(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y_vals, label=r'$F(x)$ con $C=0$', color='b', linewidth=2)
plt.title('Antiderivada del Problema 34')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P34_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
