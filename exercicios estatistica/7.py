from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Parâmetros fornecidos
mu = 67  # velocidade média (mph)
sigma = 3.5  # desvio padrão (mph)
limite = 70  # limite de velocidade (mph)

# a) Esboçar um gráfico
plt.figure(figsize=(10, 6))
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

plt.plot(x, y, 'b-', label=f'Distribuição Normal (μ={mu}, σ={sigma})')
plt.fill_between(x, y, where=(x >= limite), color='red', alpha=0.3,
                label=f'P(X > {limite})')

plt.axvline(mu, color='g', linestyle='--', label=f'Média = {mu} mph')
plt.axvline(limite, color='r', linestyle='-', label=f'Limite = {limite} mph')

plt.title('Distribuição de Velocidades dos Veículos')
plt.xlabel('Velocidade (mph)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

# b) Determinar o escore-z correspondente a 70 mph
z = (limite - mu) / sigma

# c) Encontrar a área à direita do escore-z
probabilidade = 1 - norm.cdf(z)

# Resultados
print("Resolução passo a passo:")
print(f"b) Escore-z para {limite} mph: z = ({limite} - {mu}) / {sigma} = {z:.3f}")
print(f"c) Área à direita de z = {z:.3f}: {probabilidade:.4f} ou {probabilidade*100:.2f}%")

# d) Interpretação dos resultados
print("\nInterpretação:")
print(f"A probabilidade de um veículo estar acima do limite de {limite} mph é de {probabilidade*100:.2f}%")
print(f"Isso significa que aproximadamente {int(round(probabilidade*100))} em cada 100 veículos ultrapassam o limite")