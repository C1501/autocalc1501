import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio para la función y la antiderivada (evitando singularidades)
x = np.linspace(0.1, 2.5, 400)

# Antiderivada F(x) con C = 0
def F(x):
    z = np.tan(x / 2.0)
    # Evitar división por cero o logaritmos de números negativos
    val = z / (z + 2.0)
    return 0.5 * np.log(np.abs(val))

y = F(x)

plt.figure(figsize=(6, 3.5))
plt.plot(x, y, label=r'$F(x)$ con $C=0$', color='blue', linewidth=2)
plt.title(r'Gráfica de la Antiderivada $F(x)$')
plt.xlabel(r'$x$')
plt.ylabel(r'$F(x)$')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='best')
plt.tight_layout()

plt.savefig(r'semana_04/graficas/SEM04_P12_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
