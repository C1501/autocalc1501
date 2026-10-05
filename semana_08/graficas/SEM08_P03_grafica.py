import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el intervalo [x, y]
x_val = 1.0
y_val = 3.0

# Generar puntos para la función F(x) = ln(x) con C = 0
t = np.linspace(0.4, 4.0, 400)
F = np.log(t)

# Puntos extremos para la secante
sec_x = np.array([x_val, y_val])
sec_y = np.log(sec_x)

# Encontrar c donde la pendiente de la secante es igual a f'(c)
# f'(c) = (ln(y) - ln(x)) / (y - x) = 1/c => c = (y - x) / (ln(y) - ln(x))
slope = (np.log(y_val) - np.log(x_val)) / (y_val - x_val)
c_val = 1.0 / slope
fc_val = np.log(c_val)

# Crear la figura
plt.figure(figsize=(4, 3))

# Graficar la curva con la etiqueta requerida especificando C = 0
plt.plot(t, F, label=r'$F(x)$ con $C=0$', color='blue')

# Graficar la recta secante
plt.plot(sec_x, sec_y, 'r--', label=r'Recta Secante')

# Marcar el punto c y su derivada
plt.scatter([c_val], [fc_val], color='black', zorder=5)
plt.annotate(r'$c$', (c_val, fc_val), textcoords="offset points", xytext=(0,10), ha='center')

# Configuración de ejes y gráfica
plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')
plt.axvline(0, color='gray', linewidth=0.8, linestyle='--')
plt.xlim(0.2, 4.5)
plt.ylim(-1.5, 2.0)
plt.xlabel(r'$t$')
plt.ylabel(r'$f(t)$')
plt.legend(loc='upper left', fontsize=8)
plt.grid(True, linestyle=':', alpha=0.6)

# Ajustar diseño y guardar
plt.tight_layout()
plt.savefig('grafica_problema.pdf')
plt.close()
plt.savefig(r'semana_08/graficas/SEM08_P03_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
