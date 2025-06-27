import math
from scipy.stats import norm

# Dados
n = 75
p = 0.32
q = 1 - p
x = 15

# a. Verificar se pode usar normal
np_ = n * p
nq = n * q
usa_normal = np_ >= 5 and nq >= 5
print(f"a. Pode usar aproximação normal? {usa_normal} (np = {np_:.2f}, nq = {nq:.2f})")

# b. Média e desvio padrão
mu = np_
sigma = math.sqrt(n * p * q)
print(f"b. Média (μ) = {mu:.2f}, Desvio padrão (σ) = {sigma:.2f}")

# c. Correção de continuidade: P(X = 15) -> P(14.5 < X < 15.5)
x1 = 14.5
x2 = 15.5

# d. Calcular escores-z
z1 = (x1 - mu) / sigma
z2 = (x2 - mu) / sigma
print(f"c. Escore-z para 14.5: z1 = {z1:.2f}")
print(f"   Escore-z para 15.5: z2 = {z2:.2f}")

# e. Calcular área sob a curva normal
p_z1 = norm.cdf(z1)
p_z2 = norm.cdf(z2)
prob = p_z2 - p_z1
print(f"d. P(14.5 < X < 15.5) ≈ P({z1:.2f} < Z < {z2:.2f}) = {prob:.4f} ({prob*100:.2f}%)")
