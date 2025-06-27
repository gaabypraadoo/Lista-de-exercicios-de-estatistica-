from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Definindo o escore-z
z = -2.16

# a) Desenhar a curva normal padrão e sombrear a área à direita de z = -2.16
plt.figure(figsize=(10, 6))
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)

# Plotando a curva normal
plt.plot(x, y, 'b-', label='Curva Normal Padrão (μ=0, σ=1)')

# Sombreando a área à direita de z
plt.fill_between(x, y, where=(x >= z), color='red', alpha=0.3, 
                label=f'Área à direita de z={z}')

# Linha vertical no ponto z
plt.axvline(z, color='k', linestyle='--', label=f'z = {z}')
plt.axvline(0, color='g', linestyle=':', label='μ = 0')

# Configurações do gráfico
plt.title('Área sob a Curva Normal Padrão à Direita de z = -2.16')
plt.xlabel('Escore-z')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

# b) Encontrar a área à esquerda de z = -2.16 usando a tabela normal padrão
area_left = norm.cdf(z)

# c) Subtrair a área de 1 para obter a área à direita
area_right = 1 - area_left

# Resultados
print("Resolução passo a passo:")
print(f"b) Área à esquerda de z = {z}: {area_left:.4f} (usando norm.cdf)")
print(f"c) Área à direita de z = {z}: 1 - {area_left:.4f} = {area_right:.4f}")

print("\nRespostas finais:")
print(f"A área sob a curva normal padrão à direita de z = -2.16 é: {area_right:.4f} ou {area_right*100:.2f}%")

# Comparação com a tabela normal padrão
print("\nComparação com a tabela normal padrão:")
print("1. Na tabela, procurar o valor absoluto |2.16| → aproximadamente 0.9846")
print("2. Para z negativo, área à esquerda = 1 - 0.9846 = 0.0154")
print("3. Área à direita = 1 - 0.0154 = 0.9846")
print(f"Resultado Python: {area_right:.4f}")