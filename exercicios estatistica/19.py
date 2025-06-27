from scipy.stats import norm
import numpy as np

# Parâmetros da população
mu = 190         # média
sigma = 48       # desvio padrão
x = 200          # valor que queremos calcular a probabilidade

# 1. Probabilidade de um único monitor custar menos de $200
z1 = (x - mu) / sigma
p1 = norm.cdf(z1)

# 2. Probabilidade da média de 10 monitores custar menos de $200
n = 10
sigma_amostral = sigma / np.sqrt(n)
z2 = (x - mu) / sigma_amostral
p2 = norm.cdf(z2)

# Exibindo os resultados
print(f"1. P(preço < $200) para 1 monitor = {p1:.4f} ({p1*100:.2f}%)")
print(f"2. P(média < $200) para 10 monitores = {p2:.4f} ({p2*100:.2f}%)")

print("\nComparação:")
if p2 > p1:
    print("A probabilidade da média ser menor que $200 é MAIOR do que para um único monitor.")
else:
    print("A probabilidade da média ser menor que $200 é MENOR do que para um único monitor.")
