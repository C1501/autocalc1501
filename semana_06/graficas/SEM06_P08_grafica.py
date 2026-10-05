import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def generar_grafico():
    x = np.linspace(-0.2, 1.2, 400)
    y = x**2 + 2*x - 1
    F = (x**3)/3 + x**2 - x  # Antiderivada con C = 0

    plt.figure(figsize=(6, 3.5))
    
    # Curva de la función integrandas
    plt.plot(x, y, label=r'$f(x) = x^2 + 2x - 1$', color='b', linewidth=2)
    
    # Curva de la antiderivada con C=0 requerida por regla 8
    plt.plot(x, F, label=r'$F(x)$ con $C=0$', color='r', linestyle='--', linewidth=2)
    
    # Rellenar el área bajo la curva de la integral definida de 0 a 1
    x_fill = np.linspace(0, 1, 100)
    y_fill = x_fill**2 + 2*x_fill - 1
    plt.fill_between(x_fill, y_fill, color='gray', alpha=0.3, label=r'Área $= 1/3$')

    plt.axhline(0, color='black', linewidth=0.8, linestyle='-')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='-')
    plt.axvline(1, color='green', linewidth=1, linestyle=':', label=r'$x = 1$')
    
    plt.title(r'Interpretación Geométrica de $\int_{0}^{1} (x^2 + 2x - 1) dx$', fontsize=10)
    plt.xlabel('$x$', fontsize=9)
    plt.ylabel('$y$', fontsize=9)
    plt.legend(fontsize=8, loc='upper left')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.xlim(-0.2, 1.2)
    plt.ylim(-1.5, 2.5)
    plt.tight_layout()
    plt.savefig('SEM06_P08_grafico.png', dpi=300)
    plt.close()

if __name__ == '__main__':
    generar_grafico()
plt.savefig(r'semana_06/graficas/SEM06_P08_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
