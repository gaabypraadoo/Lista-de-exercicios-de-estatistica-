import math
from scipy.stats import norm

# a. Dados do problema
n = 30                # tamanho da amostra
x_barra = 22.9        # média amostral
sigma = 1.5           # desvio padrão populacional
conf = 0.90           # nível de confiança

# zc (área central de 90% → 5% em cada cauda → 0.95 à esquerda)
zc = norm.ppf((1 + conf) / 2)

# Margem de erro
E = zc * (sigma / math.sqrt(n))

# b. Limites do intervalo
limite_inferior = x_barra - E
limite_superior = x_barra + E

# Resultados
print(f"a. n = {n}, x̄ = {x_barra}, σ = {sigma}, zc = {zc:.4f}, E = {E:.4f}")
print(f"b. Intervalo de confiança de 90%: ({limite_inferior:.2f}, {limite_superior:.2f})")
print("c. Interpretação: Com 90% de confiança, a média de idade dos estudantes está")
print(f"   entre {limite_inferior:.2f} e {limite_superior:.2f} anos.")
