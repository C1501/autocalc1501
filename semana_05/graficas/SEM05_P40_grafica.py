import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio para x, evitando valores extremos para la visualización clara
x = np.linspace(-3, 3, 400)

# Antiderivada F(x) con C = 0
F_x = (x / 2.0) * np.sqrt(1 + x**2) - 0.5 * np.log(np.abs(x + np.sqrt(1 + x**2)))

# Configuración de la figura para una columna en formato IEEE
plt.figure(figsize=(3.5, 2.5))

# Graficar la función asegurando que la etiqueta indique C = 0
plt.plot(x, F_x, 'b-', label=r'$F(x)$ con $C=0$')

# Configuración de ejes y etiquetas
plt.title(r'Gráfica de la antiderivada', fontsize=9)
plt.xlabel(r'$x$', fontsize=8)
plt.ylabel(r'$F(x)$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8)

# Ajustar límites y diseño
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.tight_layout()

# Guardar la imagen con resolución adecuada para IEEE
plt.savefig('SEM05_P40_grafica.png', dpi=300)
plt.close()
plt.savefig(r'semana_05/graficas/SEM05_P40_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
