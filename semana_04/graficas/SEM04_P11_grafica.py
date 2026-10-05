import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Generar valores para x evitando las asíntotas donde cos(x) + sin(x) = 0
x = np.linspace(-2.0, 2.0, 400)
# Asíntota principal ocurre en x = -pi/4 approx -0.785
# Restringimos el dominio para graficar una rama principal continua
x = np.linspace(-2.0, 0.5, 400)

# Función integrando f(x) = 1 / (cos(x) + sin(x))
y_integrand = 1.0 / (np.cos(x) + np.sin(x))

# Antiderivada F(x) con C = 0
# F(x) = (1/sqrt(2)) * ln | (sqrt(2) - cos(x) + sin(x)) / (sin(x) + cos(x)) |
numerador = np.sqrt(2) - np.cos(x) + np.sin(x)
denominador = np.sin(x) + np.cos(x)
y_antideriv = (1.0 / np.sqrt(2)) * np.log(np.abs(numerador / denominador))

plt.figure(figsize=(3.5, 2.5))
plt.plot(x, y_integrand, label=r'$f(x)$', color='blue', linestyle='--')
plt.plot(x, y_antideriv, label=r'$F(x)$ con $C=0$', color='red')

plt.ylim(-6, 6)
plt.title(r'Gráfica para el Problema 11', fontsize=9)
plt.xlabel(r'$x$', fontsize=8)
plt.ylabel(r'$y$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend(fontsize=7, loc='upper right')
plt.grid(True, linestyle=':', alpha=0.6)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()
plt.savefig(r'semana_04/graficas/SEM04_P11_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
