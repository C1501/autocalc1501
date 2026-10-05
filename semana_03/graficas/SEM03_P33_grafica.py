import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio evitando la asíntota vertical en x = -1 y x = 1
x = np.linspace(-3.5, 3.5, 800)
x = x[(x != -1) & (x != 1)]

# Definición de la antiderivada F(x) con C = 0
# F(x) = 2x^2 - 6x + (25/4)*ln|x+1| - 3/(2(x+1)) + (11/4)*ln|x-1|
F = 2*x**2 - 6*x + (25/4)*np.log(np.abs(x + 1)) - 3/(2*(x + 1)) + (11/4)*np.log(np.abs(x - 1))

plt.figure(figsize=(6, 4))
plt.plot(x, F, 'b-', label=r'$F(x)$ con $C=0$')
plt.axvline(x=-1, color='r', linestyle='--', alpha=0.6, label='Asíntotas')
plt.axvline(x=1, color='r', linestyle='--', alpha=0.6)

plt.title('Gráfica de la Antiderivada')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.ylim(-30, 30)
plt.legend(loc='upper center')
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.savefig(r'semana_03/graficas/SEM03_P33_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
