import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

n = 5
t = np.linspace(1, n, 400)
f = 1 / t
F = np.log(t)  # Antiderivada con C = 0

plt.figure(figsize=(4, 3))
plt.plot(t, F, label=r'$F(x)$ con $C=0$', color='blue', linewidth=1.5)
plt.plot(t, f, label=r'$f(t) = 1/t$', color='red', linestyle='--', linewidth=1.2)

for k in range(1, n):
    plt.bar(k, 1/k, width=1.0, align='edge', facecolor='orange', 
            edgecolor='black', alpha=0.3, linewidth=0.8)

plt.title('Comparación Sumas de Riemann e Integral', fontsize=9)
plt.xlabel('$t$', fontsize=8)
plt.ylabel('$y$', fontsize=8)
plt.xlim(1, n)
plt.ylim(0, 1.5)
plt.axhline(0, color='black', linewidth=0.8)
plt.legend(fontsize=7, loc='upper right')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.savefig(r'semana_08/graficas/SEM08_P04_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
