import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio para la visualización
x = np.linspace(1.2, 5.0, 400)

# Antiderivada aproximada F(x) con C = 0 para efectos de graficación
# Representa el comportamiento de la integral evaluada
F = (5.0/9.0) * np.log(np.abs(x - 1)) - (5.0/9.0) * np.log(np.abs(x + 2)) + \
    (2.0/3.0) / (x + 2) + np.arcsinh((2*x + 1)/np.sqrt(3)) / 6.0

plt.figure(figsize=(6, 4))
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='b', linewidth=2)
plt.title(r'Gráfica de la Antiderivada $F(x)$ (Problema 19)')
plt.xlabel(r'$x$')
plt.ylabel(r'$F(x)$')
plt.grid(True)
plt.legend(loc='best')
plt.tight_layout()

plt.savefig(r'semana_05/graficas/SEM05_P19_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
