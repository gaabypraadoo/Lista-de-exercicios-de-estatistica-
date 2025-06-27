import math
from scipy.stats import norm

# Dados do problema
sigma = 7.9       # desvio padrão populacional
E = 2.0           # margem de erro máxima
conf_level = 0.95 # nível de confiança

# Calcula o valor crítico Z para o nível de confiança
alpha = 1 - conf_level
Z = norm.ppf(1 - alpha/2)  # quantil da normal padrão

# Calcula o tamanho da amostra
n = (Z * sigma / E) ** 2

# Mostra o resultado arredondado para cima (não faz sentido ter fração de pessoa)
n_ceil = math.ceil(n)

print(f"Tamanho da amostra necessário: {n_ceil} funcionários")
