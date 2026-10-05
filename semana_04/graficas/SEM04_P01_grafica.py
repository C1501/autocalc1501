import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de x evitando las asíntotas y discontinuidades
# Para 1 + tan(x/2) = 0 -> tan(x/2) = -1 -> x/2 = -pi/4 + k*pi -> x = -pi/2 + 2*k*pi
# Además cos(x) + sin(x) + 1 = 0 en x = -pi/2 y x = pi
x = np.linspace(-1.4, 1.2, 400)

# Antiderivada con C = 0: F(x) = ln|1 + tan(x/2)|
# Usamos np.abs para evitar errores con valores negativos antes del logaritmo
F = np.log(np.abs(1.0 + np.tan(x / 2.0)))

plt.figure(figsize=(3.5, 2.5))
plt.plot(x, F, 'b-', label=r'$F(x)$ con $C=0$')
plt.title('Antiderivada de la integral', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$F(x)$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8)
plt.tight_layout()

plt.savefig(r'semana_04/graficas/SEM04_P01_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
