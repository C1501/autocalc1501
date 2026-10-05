import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio evitando singularidades en x^3 = -1 y x^3 = -8
x = np.linspace(-1.8, 1.8, 400)

# Antiderivada F(x) con C = 0
# F(x) = (1/21) * ln( |(x^3 + 8)^8 / (x^3 + 1)| )
# Para evitar problemas con valores negativos o división por cero en el dominio de trazado:
# Excluimos vecindades de x = -1 y x = -2 (pues (-2)^3 = -8)
mask = (x > -1.9) & (x < -0.9) | (x > -0.9)
x_plot = np.linspace(-1.85, 1.85, 600)
# Filtramos de manera segura para la visualización
y_vals = []
x_vals = []
for val in x_plot:
    # Evitar singularidades exactas
    if abs(val + 1.0) > 0.02 and abs(val + 2.0) > 0.02:
        val_arg = ((val**3 + 8)**8) / abs(val**3 + 1)
        if val_arg > 0:
            y_vals.append((1.0 / 21.0) * np.log(val_arg))
            x_vals.append(val)

x_vals = np.array(x_vals)
y_vals = np.array(y_vals)

plt.figure(figsize=(6, 3.5))
plt.plot(x_vals, y_vals, label=r'$F(x)$ con $C=0$', color='b', linewidth=2)

plt.title('Gráfica de la Antiderivada (Problema 38)', fontsize=10)
plt.xlabel('$x$', fontsize=9)
plt.ylabel('$F(x)$', fontsize=9)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=9)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P38_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
