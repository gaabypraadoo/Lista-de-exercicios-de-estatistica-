from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Parâmetros assumidos baseados em valores médicos típicos
mu = 120    # nível médio de triglicerídeos (mg/dL)
sigma = 30  # desvio padrão (mg/dL)
min_level = 100  # limite inferior (mg/dL)
max_level = 150  # limite superior (mg/dL)

# a) Esboçar um gráfico
plt.figure(figsize=(10, 6))
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

plt.plot(x, y, 'b-', label=f'Distribuição Normal (μ={mu}, σ={sigma})')
plt.fill_between(x, y, where=(x >= min_level) & (x <= max_level), 
                 color='purple', alpha=0.3,
                 label=f'P({min_level} ≤ X ≤ {max_level})')

plt.axvline(mu, color='black', linestyle='--', label=f'Média = {mu} mg/dL')
plt.axvline(min_level, color='red', linestyle=':', label=f'Limite inferior = {min_level} mg/dL')
plt.axvline(max_level, color='red', linestyle=':', label=f'Limite superior = {max_level} mg/dL')

plt.title('Distribuição dos Níveis de Triglicerídeos na População dos EUA')
plt.xlabel('Nível de Triglicerídeos (mg/dL)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

# b) Calcular os escores-z
z_min = (min_level - mu) / sigma
z_max = (max_level - mu) / sigma

# c) Encontrar as áreas acumuladas e calcular a diferença
area_min = norm.cdf(z_min)
area_max = norm.cdf(z_max)
probabilidade = area_max - area_min

# Resultados
print("Resolução passo a passo:")
print(f"Escore-z para {min_level} mg/dL: z = ({min_level} - {mu}) / {sigma} = {z_min:.3f}")
print(f"Escore-z para {max_level} mg/dL: z = ({max_level} - {mu}) / {sigma} = {z_max:.3f}")
print(f"\nÁrea acumulada até {min_level} mg/dL: {area_min:.5f}")
print(f"Área acumulada até {max_level} mg/dL: {area_max:.5f}")
print(f"Diferença (probabilidade): {area_max:.5f} - {area_min:.5f} = {probabilidade:.5f}")

# Interpretação
print("\nResultado final:")
print(f"A probabilidade de um indivíduo ter nível de triglicerídeos entre {min_level} e {max_level} mg/dL é de {probabilidade*100:.2f}%")

print("\nObservação importante:")
print("Os valores de média (μ=120) e desvio padrão (σ=30) foram assumidos para este exercício")
print("pois não foram fornecidos no enunciado. Em uma situação real, utilize os parâmetros")
print("específicos da população em estudo.")