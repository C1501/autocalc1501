import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de la función (evitando valores donde el denominador se anule, aunque sin(x) nunca es 2)
x = np.linspace(-np.pi, np.pi, 500)

# Función integranda original
def integrand(x):
    return (np.cos(x)**3) / (2 - np.sin(x))

# Antiderivada con C = 0
def antiderivative(x):
    u = np.sin(x)
    return 0.5 * u**2 + 2 * u + 3 * np.log(2 - u)

y_integrand = integrand(x)
y_antideriv = antiderivative(x)

plt.figure(figsize=(6, 3.5))
plt.plot(x, y_integrand, label=r'Integrando $\frac{\cos^3 x}{2 - \sin x}$', color='crimson', linestyle='--')
plt.plot(x, y_antideriv, label=r'$F(x)$ con $C=0$', color='navy', linewidth=2)

plt.title(r'Gráfica de la función y su antiderivada (Prob 20)', fontsize=10)
plt.xlabel('$x$', fontsize=9)
plt.ylabel('$y$', fontsize=9)
plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.legend(fontsize=8, loc='upper left')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.savefig(r'semana_04/graficas/SEM04_P20_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
