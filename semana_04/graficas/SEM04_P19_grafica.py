import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de la función, evitando ceros y singularidades
x = np.linspace(0.1, np.pi - 0.1, 400)

# Antiderivada F(x) con C = 0
# F(x) = ln( |sin(x) / (1 + sin(x))^2| )
sin_x = np.sin(x)
with np.errstate(divide='ignore', invalid='ignore'):
    F_x = np.log(np.abs(sin_x / (1.0 + sin_x)**2))

# Configuración de la gráfica para dos columnas IEEE
plt.figure(figsize=(3.5, 2.5))
plt.plot(x, F_x, label=r'$F(x)$ con $C=0$', color='blue', linewidth=1.5)

plt.title('Gráfica de la Antiderivada', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$F(x)$', fontsize=8)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=8)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()


plt.savefig(r'semana_04/graficas/SEM04_P19_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
