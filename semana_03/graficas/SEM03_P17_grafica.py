import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio evitando la asíntota x = 1 y x = 2
x1 = np.linspace(-1, 0.95, 400)
x2 = np.linspace(1.05, 1.95, 400)
x3 = np.linspace(2.05, 4.0, 400)

# Antiderivada F(x) con C = 0
def F(x):
    return 10 * np.log(np.abs(x - 2)) - 9 * np.log(np.abs(x - 1)) + 7 / (x - 1)

y1 = F(x1)
y2 = F(x2)
y3 = F(x3)

# Configuración de la gráfica para dos columnas IEEE
plt.figure(figsize=(3.5, 2.8))

plt.plot(x1, y1, 'b-', label=r'$F(x)$ con $C=0$')
plt.plot(x2, y2, 'b-')
plt.plot(x3, y3, 'b-')

plt.axvline(x=1, color='r', linestyle='--', alpha=0.6, label='Asintotas')
plt.axvline(x=2, color='r', linestyle='--', alpha=0.6)

plt.title('Antiderivada del Problema 17', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$F(x)$', fontsize=8)
plt.ylim(-20, 20)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=7, loc='lower right')

plt.tight_layout()
plt.savefig('SEM03_P17_grafica.png', dpi=300)
plt.close()
plt.savefig(r'semana_03/graficas/SEM03_P17_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
