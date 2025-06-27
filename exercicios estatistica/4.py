from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Definindo o escore-z
z = 2.13

# Calculando a área à esquerda de z
area = norm.cdf(z)  # Função de distribuição acumulada

# Criando o gráfico
plt.figure(figsize=(10, 6))

# Gerando pontos para a curva normal padrão
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)

# Plotando a curva normal
plt.plot(x, y, 'b-', label='Curva Normal Padrão (μ=0, σ=1)')

# Sombreando a área à esquerda de z
plt.fill_between(x, y, where=(x <= z), color='red', alpha=0.3, 
                label=f'Área à esquerda de z={z}: {area:.4f}')

# Linha vertical no ponto z
plt.axvline(z, color='k', linestyle='--', label=f'z = {z}')

# Configurações do gráfico
plt.title('Área sob a Curva Normal Padrão à Esquerda de z = 2.13')
plt.xlabel('Escore-z')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

# Resultados
print("Respostas:")
print(f"a) Gráfico mostrando a curva normal com a área à esquerda de z=2.13 sombreada")
print(f"b) A área à esquerda de z = {z} é: {area:.4f} ou {area*100:.2f}%")

# Comparação com a tabela normal padrão
print("\nComparação com a tabela normal padrão:")
print("Na tabela normal padrão, o valor para z=2.13 é aproximadamente 0.9834")
print(f"Nosso cálculo usando Python: {area:.4f}")