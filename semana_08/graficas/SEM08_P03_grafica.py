import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el intervalo [x, y]
x_val = 1.0
y_val = 3.0

# Generar puntos para la función f(t) = ln(t)
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

# Crear la figura (formato IEEE)
plt.figure(figsize=(3.5, 2.5))

# Graficar la curva
plt.plot(t, F, label=r'$f(t) = \ln(t)$', color='blue')

# Graficar la recta secante
plt.plot(sec_x, sec_y, 'r--', label=r'Recta Secante')

# Marcar el punto c
plt.scatter([c_val], [fc_val], color='black', zorder=5)
plt.annotate(r'$c$', (c_val, fc_val), textcoords="offset points", xytext=(0, 10), ha='center')

# Configuración de ejes y gráfica
plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')
plt.axvline(0, color='gray', linewidth=0.8, linestyle='--')
plt.xlim(0.2, 4.5)
plt.ylim(-1.5, 2.0)
plt.xlabel(r'$t$', fontsize=9)
plt.ylabel(r'$f(t)$', fontsize=9)
plt.legend(loc='upper left', fontsize=7)
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()

# Guardar ÚNICAMENTE una vez en la ruta correcta antes del plt.close()
plt.savefig(r'semana_08/graficas/SEM08_P03_grafica.png', dpi=300, bbox_inches='tight')
plt.close()