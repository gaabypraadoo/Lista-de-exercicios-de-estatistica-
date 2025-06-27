import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros populacionais
mu = 47    # média populacional (US$)
sigma = 9  # desvio padrão populacional (US$)
n = 64     # tamanho da amostra

# a) Calcular a média e o desvio padrão da distribuição amostral
mu_amostral = mu  # A média da distribuição amostral é igual à média populacional
sigma_amostral = sigma / np.sqrt(n)  # Erro padrão da média

print("Resolução:")
print(f"Média da distribuição amostral (μ_x̄): {mu_amostral} US$")
print(f"Desvio padrão da distribuição amostral (σ_x̄): σ/√n = {sigma}/√{n} = {sigma_amostral:.3f} US$")

# b) Esboçar um gráfico da distribuição amostral
plt.figure(figsize=(12, 6))
x = np.linspace(mu - 4*sigma_amostral, mu + 4*sigma_amostral, 1000)
y = norm.pdf(x, mu_amostral, sigma_amostral)

plt.plot(x, y, 'b-', linewidth=2, label=f'Distribuição Amostral (μ={mu_amostral}, σ={sigma_amostral:.3f})')
plt.axvline(mu_amostral, color='red', linestyle='--', label=f'Média = {mu_amostral} US$')

# Marcar intervalos de 1, 2 e 3 desvios padrão
for i in range(1, 4):
    plt.axvline(mu_amostral + i*sigma_amostral, color='green', linestyle=':', alpha=0.5)
    plt.axvline(mu_amostral - i*sigma_amostral, color='green', linestyle=':', alpha=0.5)

plt.title('Distribuição Amostral das Médias das Contas de Telefone Celular (n=64)')
plt.xlabel('Média Amostral (US$)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

# Explicação do Teorema do Limite Central
print("\nExplicação:")
print("1. Pelo Teorema do Limite Central, a distribuição amostral das médias será:")
print("   - Normalmente distribuída (mesmo que a população não seja)")
print("   - Com média igual à média populacional (μ_x̄ = μ)")
print("   - Com desvio padrão igual a σ/√n (erro padrão)")

print("\n2. Para n=64:")
print(f"   - μ_x̄ = {mu} US$ (mesmo valor da população)")
print(f"   - σ_x̄ = {sigma}/√64 = {sigma}/8 = {sigma_amostral:.3f} US$")

print("\n3. Interpretação:")
print(f"   - 68% das médias amostrais estarão entre {mu-sigma_amostral:.2f} e {mu+sigma_amostral:.2f} US$")
print(f"   - 95% das médias amostrais estarão entre {mu-2*sigma_amostral:.2f} e {mu+2*sigma_amostral:.2f} US$")
print(f"   - 99.7% das médias amostrais estarão entre {mu-3*sigma_amostral:.2f} e {mu+3*sigma_amostral:.2f} US$")