import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros populacionais
mu = 3.5     # média populacional (pés)
sigma = 0.2  # desvio padrão populacional (pés)
n = 16       # tamanho da amostra

# a) Calcular a média e o erro padrão da distribuição amostral
mu_amostral = mu  # A média da distribuição amostral é igual à média populacional
sigma_amostral = sigma / np.sqrt(n)  # Erro padrão da média

print("Resolução:")
print(f"Média da distribuição amostral (μ_x̄): {mu_amostral} pés")
print(f"Erro padrão da distribuição amostral (σ_x̄): σ/√n = {sigma}/√{n} = {sigma_amostral:.4f} pés")

# b) Esboçar uma curva normal com os parâmetros da distribuição amostral
plt.figure(figsize=(12, 6))
x = np.linspace(mu - 4*sigma_amostral, mu + 4*sigma_amostral, 1000)
y = norm.pdf(x, mu_amostral, sigma_amostral)

plt.plot(x, y, 'b-', linewidth=2, label=f'Distribuição Amostral (μ={mu_amostral}, σ={sigma_amostral:.4f})')
plt.axvline(mu_amostral, color='red', linestyle='--', label=f'Média = {mu_amostral} pés')

# Marcar intervalos de 1, 2 e 3 erros padrão
for i in range(1, 4):
    plt.axvline(mu_amostral + i*sigma_amostral, color='green', linestyle=':', alpha=0.5,
               label=f'±{i}σ_x̄' if i == 1 else '')
    plt.axvline(mu_amostral - i*sigma_amostral, color='green', linestyle=':', alpha=0.5)

plt.title('Distribuição Amostral das Médias dos Diâmetros de Carvalhos (n=16)')
plt.xlabel('Diâmetro Médio Amostral (pés)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

# Explicação detalhada
print("\nExplicação do Teorema do Limite Central:")
print("1. A distribuição amostral das médias tem:")
print(f"   - Média (μ_x̄) = μ = {mu} pés")
print(f"   - Erro padrão (σ_x̄) = σ/√n = {sigma}/√{n} = {sigma}/4 = {sigma_amostral:.4f} pés")

print("\n2. Para amostras de tamanho n=16:")
print(f"   - 68% das médias amostrais estarão entre {mu-sigma_amostral:.3f} e {mu+sigma_amostral:.3f} pés")
print(f"   - 95% das médias amostrais estarão entre {mu-2*sigma_amostral:.3f} e {mu+2*sigma_amostral:.3f} pés")
print(f"   - 99.7% das médias amostrais estarão entre {mu-3*sigma_amostral:.3f} e {mu+3*sigma_amostral:.3f} pés")

print("\n3. Comparação com a população:")
print(f"   População: σ = {sigma} pé (variabilidade individual)")
print(f"   Médias amostrais (n=16): σ_x̄ = {sigma_amostral:.4f} pé (variabilidade das médias)")
print("   A variabilidade das médias é menor que a variabilidade individual")