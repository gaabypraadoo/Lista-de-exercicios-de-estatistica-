import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Como a figura 5.8 não foi fornecida, faremos suposições baseadas em testes padronizados típicos
# Vamos assumir que a distribuição das notas segue um padrão comum com média 650 e desvio padrão 50
# (Valores hipotéticos, pois a figura não está disponível)

# Parâmetros da distribuição normal
mu = 650  # média
sigma = 50  # desvio padrão

# Criando pontos para o eixo x (notas)
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# Calculando a PDF (Probability Density Function)
pdf = norm.pdf(x, mu, sigma)

# Plotando a curva normal
plt.figure(figsize=(10, 6))
plt.plot(x, pdf, 'b-', label=f'Distribuição das notas: μ={mu}, σ≈{sigma}')
plt.axvline(mu, color='r', linestyle='--', label=f'Média (μ) = {mu}')

# Marcando pontos importantes
plt.axvline(mu + sigma, color='g', linestyle=':', alpha=0.5, label=f'μ+σ = {mu+sigma}')
plt.axvline(mu - sigma, color='g', linestyle=':', alpha=0.5, label=f'μ-σ = {mu-sigma}')

plt.title('Distribuição das Notas Padronizadas do Teste de Linguagem do 8º Ano')
plt.xlabel('Notas')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

# Respondendo às perguntas do exercício
print("\nRespostas:")
print(f"A nota média do teste é: {mu}")
print(f"Estimativa do desvio padrão: aproximadamente {sigma} pontos")

print("\nMétodo de estimativa:")
print("1. A média (μ) é o ponto central da distribuição, onde a curva atinge seu pico")
print("2. O desvio padrão (σ) pode ser estimado pela distância entre a média e o ponto de inflexão da curva")
print("   (onde a curva muda de convexa para côncava), ou pela distância entre a média e μ±σ que contém ~68% dos dados")