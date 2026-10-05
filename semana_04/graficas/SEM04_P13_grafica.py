import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Definición del dominio para x evitando las asíntotas
x = np.linspace(-1.2, 1.2, 500)

# Antiderivada F(x) evaluada con C = 0
# F(x) = x/2 - ln|1 + tan(x/2)| + 0.5*ln(1 + tan(x/2)^2)
# Simplificada analíticamente como x/2 - ln|1 + tan(x/2)| - ln|cos(x/2)|
tan_half = np. tan(x / 2.0)
cos_half = np. cos(x / 2.0)
F = (x / 2.0) - np.log(np.abs(1.0 + tan_half)) - np.log(np.abs(cos_half))

plt.figure(figsize=(6, 4))
plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='blue', linewidth=2)

plt.title('Gráfica de la antiderivada $F(x)$')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.8, linestyle='-')
plt.axvline(0, color='black', linewidth=0.8, linestyle='-')
plt.legend()
plt.tight_layout()

plt.savefig(r'semana_04/graficas/SEM04_P13_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
