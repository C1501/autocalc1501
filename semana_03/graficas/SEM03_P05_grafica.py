import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio para la gráfica
x = np.linspace(-6, 0, 400)

# Antiderivada F(x) con C = 0
# F(x) = ln(x^2 + 6x + 15) - (9/sqrt(6)) * arctan((x + 3)/sqrt(6))
def F(x):
    return np.log(x**2 + 6*x + 15) - (9 / np.sqrt(6)) * np.arctan((x + 3) / np.sqrt(6))

y = F(x)

# Configuración de la figura para columna doble IEEE
plt.figure(figsize=(3.5, 2.5))

plt.plot(x, y, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

plt.title('Gráfica de la Antiderivada', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$F(x)$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)

plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P05_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
