import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función integrando y la antiderivada (con C=0)
def integrand(x):
    return (x - 1) / (3*x**2 - 4*x + 3)

def antideriv(x):
    term1 = (1/6) * np.log(3*x**2 - 4*x + 3)
    term2 = (np.sqrt(5)/15) * np.arctan((3*x - 2)/np.sqrt(5))
    return term1 - term2

# Dominio para la gráfica
x = np.linspace(-2, 4, 400)
y_int = integrand(x)
y_ant = antideriv(x)

# Configuración de la figura para IEEE (ancho de una columna aprox.)
plt.figure(figsize=(3.5, 2.5))

plt.plot(x, y_ant, label=r'$F(x)$ con $C=0$', color='blue', linewidth=1.5)
plt.plot(x, y_int, label=r'$f(x)$ (Integrando)', color='orange', linestyle='--', linewidth=1.2)

plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.title('Gráfica de la solución', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$y$', fontsize=8)
plt.legend(fontsize=7)
plt.grid(True, linestyle=':', alpha=0.6)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)

plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P02_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
