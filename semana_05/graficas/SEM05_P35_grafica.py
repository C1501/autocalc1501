import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 * (2 + x**2)**(-2.5)

def F(x):
    return -(3*x**2 + 4) / (3 * (2 + x**2)**1.5)

x = np.linspace(-3.0, 3.0, 400)
y_integrand = f(x)
y_antideriv = F(x)

fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.plot(x, y_integrand, label=r'Integrando $f(x)$', color='tab:blue', linestyle='--')
ax.plot(x, y_antideriv, label=r'$F(x)$ con $C=0$', color='tab:orange', linewidth=2)

ax.set_title('Gráfica Problema 35', fontsize=9)
ax.set_xlabel('$x$', fontsize=8)
ax.set_ylabel('$y$', fontsize=8)
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
ax.set_ylim(-2.5, 2.5)
ax.legend(fontsize=7, loc='upper right')
ax.tick_params(axis='both', labelsize=7)
ax.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('problema_35.png', dpi=300)
plt.close()
plt.savefig(r'semana_05/graficas/SEM05_P35_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
