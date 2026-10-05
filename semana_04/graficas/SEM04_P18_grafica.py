import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio de la función en un rango seguro
x = np.linspace(-1.2, 1.2, 500)

# Función original (integrando) y su antiderivada con C = 0
# Nota: cos(x) está entre -1 y 1, por lo tanto cos(x) - 2 nunca es cero.
# Evaluamos F(x) = 1/3 * ln(|(cos(x) + 1)/(cos(x) - 2)|)
f_x = np.sin(x) / (np.cos(x)**2 - np.cos(x) - 2)
F_x = (1.0 / 3.0) * np.log(np.abs((np.cos(x) + 1) / (np.cos(x) - 2)))

plt.figure(figsize=(6, 3.5))
plt.plot(x, f_x, label=r'Integrando $f(x)$', color='blue', linestyle='--')
plt.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='red', linewidth=2)

plt.title('Gráfica de la Solución (Problema 18)')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='best', fontsize=9)
plt.tight_layout()

plt.savefig(r'semana_04/graficas/SEM04_P18_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
