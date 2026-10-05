import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio evitando las singularidades x = -1 y x = 1
x1 = np.linspace(-3, -1.05, 400)
x2 = np.linspace(-0.95, 0.95, 400)
x3 = np.linspace(1.05, 3, 400)

# Antiderivada F(x) con C = 0
def F(x):
    return 3.5 * np.log(np.abs(x + 1)) - 1.5 * np.log(np.abs(x - 1)) + 4.0 / (x + 1)

y1 = F(x1)
y2 = F(x2)
y3 = F(x3)

plt.figure(figsize=(4, 3))
plt.plot(x1, y1, 'b-', label=r'$F(x)$ con $C=0$')
plt.plot(x2, y2, 'b-')
plt.plot(x3, y3, 'b-')

plt.axvline(x=-1, color='r', linestyle='--', alpha=0.5, label='Asíntotas')
plt.axvline(x=1, color='r', linestyle='--', alpha=0.5)

plt.title('Gráfica de la Antiderivada')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.ylim(-15, 15)
plt.legend(loc='best', fontsize=8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.savefig(r'semana_03/graficas/SEM03_P21_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
