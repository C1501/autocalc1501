import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio evitando las asíntotas en x = -3, x = 1, x = 4
x = np.linspace(-2.5, 0.5, 400)

# Antiderivada F(x) con C = 0
# F(x) = 4*ln|x - 1| + 4*ln|x - 4| - 7*ln|x + 3|
# Evaluamos en el intervalo donde el argumento del logaritmo es positivo: (-3, 1)
def F(val):
    return 4 * np.log(np.abs(val - 1)) + 4 * np.log(np.abs(val - 4)) - 7 * np.log(np.abs(val + 3))

y = F(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y, label=r'$F(x)$ con $C=0$', color='b', linewidth=2)
plt.axvline(x=-3, color='r', linestyle='--', alpha=0.5, label='Asíntotas')
plt.axvline(x=1, color='r', linestyle='--', alpha=0.5)

plt.title('Gráfica de la Antiderivada (Problema 35)')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.ylim(-20, 10)
plt.legend(loc='lower right')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P35_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
