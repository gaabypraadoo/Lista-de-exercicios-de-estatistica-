from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Parâmetros fornecidos
mu = 45    # tempo médio (minutos)
sigma = 12 # desvio padrão (minutos)
min_tempo = 33  # limite inferior (minutos)
max_tempo = 60  # limite superior (minutos)

# a) Esboçar um gráfico
plt.figure(figsize=(10, 6))
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

plt.plot(x, y, 'b-', label=f'Distribuição Normal (μ={mu}, σ={sigma})')
plt.fill_between(x, y, where=(x >= min_tempo) & (x <= max_tempo), 
                 color='green', alpha=0.3,
                 label=f'P({min_tempo} ≤ X ≤ {max_tempo})')

plt.axvline(mu, color='black', linestyle='--', label=f'Média = {mu} min')
plt.axvline(min_tempo, color='red', linestyle=':', label=f'Limite inferior = {min_tempo} min')
plt.axvline(max_tempo, color='red', linestyle=':', label=f'Limite superior = {max_tempo} min')

plt.title('Distribuição do Tempo no Supermercado')
plt.xlabel('Tempo (minutos)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

# b) Calcular os escores-z
z_min = (min_tempo - mu) / sigma
z_max = (max_tempo - mu) / sigma

# c) Encontrar as áreas acumuladas e calcular a diferença
area_min = norm.cdf(z_min)
area_max = norm.cdf(z_max)
probabilidade = area_max - area_min

# Resultados
print("Resolução passo a passo:")
print(f"b) Escore-z para {min_tempo} min: z = ({min_tempo} - {mu}) / {sigma} = {z_min:.3f}")
print(f"   Escore-z para {max_tempo} min: z = ({max_tempo} - {mu}) / {sigma} = {z_max:.3f}")
print(f"c) Área acumulada até {min_tempo} min: {area_min:.5f}")
print(f"   Área acumulada até {max_tempo} min: {area_max:.5f}")
print(f"   Diferença (probabilidade): {area_max:.5f} - {area_min:.5f} = {probabilidade:.5f}")

# d) Interpretação para 150 consumidores
consumidores_esperados = round(probabilidade * 150)

print("\nInterpretação:")
print(f"A probabilidade de um consumidor ficar entre {min_tempo} e {max_tempo} minutos é de {probabilidade*100:.2f}%")
print(f"Para 150 consumidores, espera-se que aproximadamente {consumidores_esperados} permaneçam nesse intervalo de tempo")