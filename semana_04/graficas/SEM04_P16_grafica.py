import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de x evitando las asíntotas y discontinuidades
x = np.linspace(-2.0, 2.0, 400)

# Función f(x) = 1 / (1 + sin(x) + cos(x))
# Para evitar división por cero exacta en la visualización
den = 1.0 + np.sin(x) + np.cos(x)
f = np.where(np.abs(den) > 1e-4, 1.0 / den, np.nan)

# Antiderivada F(x) con C = 0
# F(x) = ln|1 + tan(x/2)|
F = np.log(np.abs(1.0 + np.tan(x / 2.0)))

plt.figure(figsize=(3.5, 2.5))
plt.plot(x, f, label=r'$f(x)$', color='blue', linewidth=1.2)
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='red', linestyle='--', linewidth=1.2)

plt.ylim(-3, 3)
plt.xlabel(r'$x$', fontsize=9)
plt.ylabel(r'$y$', fontsize=9)
plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8, loc='upper left')
plt.tight_layout()

plt.savefig('grafica_p16.png', dpi=300)
plt.close()
plt.savefig(r'semana_04/graficas/SEM04_P16_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
