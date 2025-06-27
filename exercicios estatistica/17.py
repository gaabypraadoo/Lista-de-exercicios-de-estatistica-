import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros fornecidos
mu = 25      # média populacional (minutos)
sigma = 1.5  # desvio padrão populacional (minutos)
n = 100      # tamanho da amostra
x1 = 24.7    # limite inferior
x2 = 25.5    # limite superior

# a) Usar o Teorema do Limite Central para encontrar μ_x̄ e σ_x̄
mu_amostral = mu
sigma_amostral = sigma / np.sqrt(n)

print("a) Parâmetros da distribuição amostral:")
print(f"μ_x̄ = μ = {mu_amostral} minutos")
print(f"σ_x̄ = σ/√n = {sigma}/√{n} = {sigma_amostral:.4f} minutos")

# b) Calcular os escores-z
z1 = (x1 - mu_amostral) / sigma_amostral
z2 = (x2 - mu_amostral) / sigma_amostral

print("\nb) Escores-z:")
print(f"Para x̄ = {x1}: z = ({x1} - {mu_amostral}) / {sigma_amostral:.4f} = {z1:.4f}")
print(f"Para x̄ = {x2}: z = ({x2} - {mu_amostral}) / {sigma_amostral:.4f} = {z2:.4f}")

# c) Encontrar as probabilidades
prob_z1 = norm.cdf(z1)
prob_z2 = norm.cdf(z2)
probabilidade = prob_z2 - prob_z1

print("\nc) Probabilidades acumuladas:")
print(f"P(z ≤ {z1:.4f}) = {prob_z1:.6f}")
print(f"P(z ≤ {z2:.4f}) = {prob_z2:.6f}")
print(f"P({x1} ≤ x̄ ≤ {x2}) = {prob_z2:.6f} - {prob_z1:.6f} = {probabilidade:.6f}")

# Visualização
plt.figure(figsize=(12, 6))
x = np.linspace(mu - 4*sigma_amostral, mu + 4*sigma_amostral, 1000)
y = norm.pdf(x, mu_amostral, sigma_amostral)

plt.plot(x, y, 'b-', label=f'Distribuição Amostral (μ={mu_amostral}, σ={sigma_amostral:.4f})')
plt.fill_between(x, y, where=(x >= x1) & (x <= x2), color='green', alpha=0.3,
                label=f'P({x1} ≤ x̄ ≤ {x2}) = {probabilidade*100:.2f}%')

plt.axvline(mu_amostral, color='red', linestyle='--', label='Média')
plt.axvline(x1, color='purple', linestyle=':', label=f'x̄ = {x1}')
plt.axvline(x2, color='purple', linestyle=':', label=f'x̄ = {x2}')

plt.title('Distribuição Amostral do Tempo Médio Dirigindo (n=100)')
plt.xlabel('Tempo Médio Dirigindo (minutos)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

# d) Interpretação
print("\nd) Interpretação:")
print(f"A probabilidade de que o tempo médio diário dirigindo por uma amostra de {n} motoristas")
print(f"jovens (15-19 anos) esteja entre {x1} e {x2} minutos é de {probabilidade*100:.2f}%.")
print("Isso significa que em muitas amostras de tamanho 100, esperaríamos que cerca de")
print(f"{int(round(probabilidade*100))}% delas tivessem médias entre {x1} e {x2} minutos.")