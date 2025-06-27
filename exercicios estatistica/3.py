from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Item a: Encontrar a área acumulada para z = -2.19
z_a = -2.19
area_a = norm.cdf(z_a)  # Função de distribuição acumulada

# Item b: Encontrar a área acumulada para z = 2.17
z_b = 2.17
area_b = norm.cdf(z_b)

# Criando visualizações
def plot_z_area(z, title):
    plt.figure(figsize=(10, 6))
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x)
    
    plt.plot(x, y, 'b-', label='Curva Normal Padrão')
    plt.fill_between(x, y, where=(x <= z), color='red', alpha=0.3, 
                    label=f'Área acumulada = {norm.cdf(z):.4f}')
    
    plt.axvline(z, color='k', linestyle='--')
    plt.title(f'Área acumulada para z = {z} - {title}')
    plt.xlabel('Escore-z')
    plt.ylabel('Densidade de Probabilidade')
    plt.legend()
    plt.grid(True)
    plt.show()

# Plotando os gráficos
plot_z_area(z_a, "Item a")
plot_z_area(z_b, "Item b")

# Resultados
print("Respostas:")
print(f"a) A área acumulada correspondente a z = {z_a} é: {area_a:.4f} ou {area_a*100:.2f}%")
print(f"b) A área acumulada correspondente a z = {z_b} é: {area_b:.4f} ou {area_b*100:.2f}%")

# Explicação adicional
print("\nComo usar a tabela normal padrão:")
print("1. Para z negativo (item a):")
print("   - Localize o valor absoluto (2.19) na tabela")
print("   - A área será 1 - valor tabelado (1 - 0.9857 = 0.0143)")
print("2. Para z positivo (item b):")
print("   - Localize diretamente o valor 2.17 na tabela (0.9850)")