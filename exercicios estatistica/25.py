import math
from scipy.stats import norm

# a. Identificar os valores
nivel_confianca = 0.95
sigma = 7.9
n = 28

# zc para 95% de confiança (área total entre -zc e +zc é 0.95)
# então queremos a área à esquerda de zc = (1 + 0.95)/2 = 0.975
zc = norm.ppf(0.975)

print(f"a. zc = {zc:.4f}, n = {n}, σ = {sigma}")

# b. Calcular margem de erro
E = zc * (sigma / math.sqrt(n))
print(f"b. Margem de erro (E) = {E:.2f} horas")

# c. Interpretar o resultado
print(f"c. Com 95% de confiança, a média de horas trabalhadas está dentro de ±{E:.2f} horas da média amostral.")
