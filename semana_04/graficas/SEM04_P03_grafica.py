import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de la función, evitando singularidades (ej. x = pi/2, 3pi/2)
x = np.linspace(0.1, 1.4, 400)

# Antiderivada F(x) con C = 0: F(x) = ln|sec(x) + 1|
F = np.log(np.abs(1.0 / np.cos(x) + 1.0))

plt.figure(figsize=(6, 4))
plt.plot(x, F, label=r'$F(x) = \ln|\sec x + 1|$ con $C=0$', color='b', linewidth=2)
plt.title(r'Antiderivada del Problema 03')
plt.xlabel(r'$x$')
plt.ylabel(r'$F(x)$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='best')
plt.tight_layout()

plt.savefig(r'semana_04/graficas/SEM04_P03_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
