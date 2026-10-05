import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función antiderivada F(x) con C = 0
# Evitamos las asíntotas donde el denominador se hace cero o indefinido
def F(x):
    z = np.tan(x / 2.0)
    numerador = z - 5
    denominador = z - 3
    # Evitar división por cero o logaritmos de números negativos/cero
    val = np.abs(numerador / denominador)
    return np.log(val)

# Generación de valores de x en un intervalo seguro
x = np.linspace(0.5, 2.0, 400)
y = F(x)

# Configuración del gráfico adaptado para dos columnas IEEE
plt.figure(figsize=(3.5, 2.5))
plt.plot(x, y, label=r'$F(x)$ con $C=0$', color='b', linewidth=1.5)

plt.title('Gráfica de la Antiderivada', fontsize=9)
plt.xlabel('$x$', fontsize=8)
plt.ylabel('$F(x)$', fontsize=8)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=8)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.tight_layout()


plt.savefig(r'semana_04/graficas/SEM04_P10_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
