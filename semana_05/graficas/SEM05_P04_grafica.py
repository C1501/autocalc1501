import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def generar_grafica():
    x = np.linspace(-2.5, 2.5, 400)
    
    # Antiderivada con C = 0
    def F(x):
        term1 = (1 + x**2)**(1.5) / 3.0
        term2 = np.sqrt(1 + x**2)
        return term1 - term2

    y = F(x)

    plt.figure(figsize=(3.5, 2.5))
    plt.plot(x, y, 'b-', label=r'$F(x)$ con $C=0$')
    
    plt.title('Gráfica de la Antiderivada', fontsize=9)
    plt.xlabel('$x$', fontsize=8)
    plt.ylabel('$F(x)$', fontsize=8)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(fontsize=8)
    plt.xticks(fontsize=7)
    plt.yticks(fontsize=7)
    plt.tight_layout()
    
    plt.savefig('grafica_sem05_p04.png', dpi=300)
    plt.close()

if __name__ == '__main__':
    generar_grafica()
plt.savefig(r'semana_05/graficas/SEM05_P04_grafica.png', dpi=300, bbox_inches='tight')
plt.close()
