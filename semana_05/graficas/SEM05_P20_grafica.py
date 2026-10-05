import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función integrando f(x)
def f(x):
    return (x + 2) / ((x - 1) * np.sqrt(x**2 + 1))

# Definición de la antiderivada F(x) con C = 0
def F(x):
    termino1 = np.log(np.abs(x + np.sqrt(x**2 + 1)))
    
    # Para evitar división por cero en x = 1
    arg_log2 = np.abs((x + 1) / (x - 1) + np.sqrt((x**2 + 1) / ((x - 1)**2)))
    termino2 = (3.0 / np.sqrt(2)) * np.log(arg_log2)
    
    return termino1 - termino2

# Evaluamos en el intervalo x > 1 para evitar la asíntota vertical en x = 1
x = np.linspace(1.1, 5.0, 400)
y_f = f(x)
y_F = F(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y_f, label=r'$f(x) = \frac{x + 2}{(x - 1)\sqrt{x^2 + 1}}$', color='crimson', linewidth=1.5)
plt.plot(x, y_F, label=r'$F(x)$ con $C=0$', color='navy', linestyle='--', linewidth=1.5)

plt.title('Gráfica de la función y su antiderivada (Problema 20)')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True, linestyle=':', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(1, color='gray', linestyle=':', label='Asíntota $x=1$')
plt.legend(loc='upper right', fontsize=8)
plt.tight_layout()

# Guardar directamente en la carpeta de la Semana 03
plt.savefig(r'semana_05/graficas/SEM05_P20_grafica.png', dpi=300, bbox_inches='tight')
plt.close()