from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Parâmetros fornecidos
mu = 11.2    # média em anos
sigma = 2.1  # desvio padrão em anos
percentil = 0.10  # 10% com menos tempo

# a) Esboçar um gráfico
plt.figure(figsize=(12, 6))
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

plt.plot(x, y, 'b-', label=f'Distribuição Normal (μ={mu}, σ={sigma})')
plt.fill_between(x, y, where=(x <= mu - sigma), color='red', alpha=0.3,
                label='10% com menos tempo')

plt.axvline(mu, color='green', linestyle='--', label='Média')
plt.title('Distribuição do Tempo de Trabalho na Empresa')
plt.xlabel('Tempo de Trabalho (anos)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

# b) Determinar o escore-z correspondente aos 10% inferiores
z = norm.ppf(percentil)

# c) Calcular x usando a fórmula x = μ + zσ
x = mu + z * sigma

# Resultados
print("Resolução passo a passo:")
print(f"b) Escore-z para o 10º percentil (área acumulada = {percentil}):")
print(f"   z = {z:.4f}")

print(f"\nc) Cálculo do tempo máximo:")
print(f"   x = μ + zσ = {mu} + ({z:.4f} × {sigma})")
print(f"   x = {x:.2f} anos")

# d) Interpretação do resultado
print("\nd) Interpretação:")
print(f"O tempo máximo que um funcionário pode ter trabalhado na empresa e ainda estar")
print(f"entre os 10% com menos tempo (e ser demitido) é de {x:.2f} anos.")
print(f"Isso significa que funcionários com menos de {x:.2f} anos de serviço serão demitidos.")
print(f"Apenas 10% dos funcionários têm tempo de serviço menor que {x:.2f} anos.")

# Comparação com a regra empírica
print("\nComparação com a regra 68-95-99.7:")
print(f"10% inferior ≈ {mu - 1.28*sigma:.2f} anos (z ≈ -1.28)")
print(f"Nosso cálculo exato: {x:.2f} anos (z = {z:.4f})")