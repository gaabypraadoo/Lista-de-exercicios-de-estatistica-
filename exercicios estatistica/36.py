from scipy.stats import norm
import math

# Dados
conf_level = 0.90
E = 0.02

# Calcula z_c para o nível de confiança
alpha = 1 - conf_level
z_c = norm.ppf(1 - alpha/2)

# Caso 1: sem estimativa preliminar (usar p̂ = 0.5)
p_hat1 = 0.5
q_hat1 = 1 - p_hat1
n1 = (z_c**2 * p_hat1 * q_hat1) / (E**2)
n1_ceil = math.ceil(n1)

# Caso 2: com estimativa preliminar p̂ = 0.31
p_hat2 = 0.31
q_hat2 = 1 - p_hat2
n2 = (z_c**2 * p_hat2 * q_hat2) / (E**2)
n2_ceil = math.ceil(n2)

# Resultados
print(f"Nivel de confiança: {conf_level*100:.0f}%")
print(f"Margem de erro E: {E*100:.1f}%")
print(f"Valor crítico z_c: {z_c:.4f}\n")

print("Caso 1 - Sem estimativa preliminar (p̂ = 0.5):")
print(f"p̂ = {p_hat1}, q̂ = {q_hat1}")
print(f"Tamanho mínimo da amostra: {n1_ceil} pessoas\n")

print("Caso 2 - Com estimativa preliminar (p̂ = 0.31):")
print(f"p̂ = {p_hat2}, q̂ = {q_hat2}")
print(f"Tamanho mínimo da amostra: {n2_ceil} pessoas")
