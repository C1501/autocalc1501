import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio para x evitando las asíntotas y discontinuidades
x = np.linspace(-2.5, 2.5, 500)

# Función integrando original f(x)
# Nota: 5 - 4*cos(x) nunca es cero ya que cos(x) >= -1, 
# por lo que el denominador varía entre 1 y 9.
def f(x):
    return 1.0 / (5.0 - 4.0 * np.cos(x))

# Antiderivada F(x) con C = 0
def F(x):
    return (2.0 / 3.0) * np.arctan(3.0 * np.tan(x / 2.0))

# Configuración de la figura para IEEE (ancho de una columna)
fig, ax = plt.subplots(figsize=(3.5, 2.5))

# Graficar curvas
ax.plot(x, f(x), label=r'$f(x)$', color='tab:blue', linestyle='--')
ax.plot(x, F(x), label=r'$F(x)$ con $C=0$', color='tab:orange', linewidth=2)

# Configuración de ejes y etiquetas
ax.set_xlabel(r'$x$', fontsize=9)
ax.set_ylabel(r'$y$', fontsize=9)
ax.axhline(0, color='black', linewidth=0.5, linestyle='-')
ax.axvline(0, color='black', linewidth=0.5, linestyle='-')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=8, loc='upper left')

# Ajustes finales de diseño
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout()

# Guardar la imagen para el documento LaTeX
plt.savefig('SEM04_P17_grafica.pdf', format='pdf', dpi=300)
plt.close()
plt.savefig(r'semana_04/graficas/SEM04_P17_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
