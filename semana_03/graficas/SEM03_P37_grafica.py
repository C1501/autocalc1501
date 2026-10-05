import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio evitando las asíntotas en x = 0, x = 1, y x = 4
x = np.linspace(-1, 5, 1000)
# Eliminar puntos muy cercanos a las singularidades para evitar saltos en la gráfica
x = x[(x < -0.05) | ((x > 0.05) & (x < 0.9)) | ((x > 1.1) & (x < 3.8)) | (x > 4.2)]

# Función original (integrando)
y_integrand = (5 * x**3 + 2) / (x**3 - 5 * x**2 + 4 * x)

# Antiderivada con C = 0
y_antideriv = (
    5 * x
    + 0.5 * np.log(np.abs(x))
    - (7.0 / 3.0) * np.log(np.abs(x - 1))
    + (161.0 / 6.0) * np.log(np.abs(x - 4))
)

plt.figure(figsize=(6, 4))
plt.plot(x, y_integrand, label="Integrando", color="red", linestyle="--")
plt.plot(x, y_antideriv, label=r"$F(x)$ con $C=0$", color="blue")

plt.axvline(0, color="gray", linestyle=":", alpha=0.7)
plt.axvline(1, color="gray", linestyle=":", alpha=0.7)
plt.axvline(4, color="gray", linestyle=":", alpha=0.7)

plt.ylim(-20, 25)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Gráfica del Integrando y la Antiderivada (Problema 37)")
plt.legend(loc="upper left")
plt.grid(True)
plt.tight_layout()

plt.savefig(r'semana_03/graficas/SEM03_P37_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
