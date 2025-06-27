from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Parâmetros da distribuição
mu = 52    # média em libras
sigma = 15 # desvio padrão em libras

# Escores-z fornecidos
z_scores = [-2.33, 3.10, 0.58]

# a) Identificar μ e σ da distribuição normal
print("a) Parâmetros da distribuição:")
print(f"Média (μ) = {mu} libras")
print(f"Desvio padrão (σ) = {sigma} libras\n")

# b) Transformar cada escore-z em um valor de peso (x)
pesos = [mu + z * sigma for z in z_scores]

print("b) Pesos correspondentes aos escores-z:")
for z, peso in zip(z_scores, pesos):
    print(f"Para z = {z:.2f} → x = {mu} + ({z:.2f} × {sigma}) = {peso:.2f} libras")

# c) Interpretar os resultados
print("\nc) Interpretação dos resultados:")
interpretacoes = [
    "Um peso 2.33 desvios padrão abaixo da média (cão significativamente abaixo do peso)",
    "Um peso 3.10 desvios padrão acima da média (cão extremamente pesado)",
    "Um peso 0.58 desvios padrão acima da média (cão levemente acima do peso médio)"
]

for z, peso, interp in zip(z_scores, pesos, interpretacoes):
    print(f"\nPara z = {z:.2f} ({peso:.2f} libras):")
    print(interp)
    print(f"Este peso está no percentil {norm.cdf(z)*100:.2f}% da distribuição")

# Visualização da distribuição com os pontos marcados
plt.figure(figsize=(12, 6))
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

plt.plot(x, y, 'b-', label=f'Distribuição Normal (μ={mu}, σ={sigma})')
plt.axvline(mu, color='green', linestyle='--', label='Média')

# Marcando os pontos correspondentes aos escores-z
colors = ['red', 'purple', 'orange']
for z, peso, color in zip(z_scores, pesos, colors):
    plt.axvline(peso, color=color, linestyle=':', 
               label=f'z={z:.2f} ({peso:.2f} lbs)')
    plt.plot(peso, norm.pdf(peso, mu, sigma), 'o', color=color)

plt.title('Distribuição de Pesos de Cães com Escores-z Destacados')
plt.xlabel('Peso (libras)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()