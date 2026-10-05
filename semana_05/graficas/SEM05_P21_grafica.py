import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio para la función y su antiderivada
x = np.linspace(-0.99, 0.99, 400)

# Antiderivada con C = 0
# F(x) = ln(|2 - 2x*sqrt(1 - x^2)|)
def F(val_x):
    inside = np.abs(2.0 - 2.0 * val_x * np.sqrt(1.0 - val_x**2))
    return np.log(inside)

y = F(x)

# Configuración de la gráfica para formato IEEE de dos columnas
plt.figure(figsize=(3.5, 2.5))
plt.plot(x, y, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

plt.title('Gráfica de la Antiderivada', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$F(x)$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)

plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P21_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
