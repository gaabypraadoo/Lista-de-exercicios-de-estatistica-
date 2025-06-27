from scipy.stats import norm
import math

# Dados
n = 498
x = 125  # arredondado de 124.5

# a) p̂ e q̂
p_hat = x / n
q_hat = 1 - p_hat
print(f"a) p̂ = {p_hat:.5f}")
print(f"   q̂ = {q_hat:.5f}")

# b) Verificação da aproximação normal
cond1 = n * p_hat >= 5
cond2 = n * q_hat >= 5
print(f"\nb) Condições para aproximação normal:")
print(f"n * p̂ = {n * p_hat:.2f} >= 5? {'Sim' if cond1 else 'Não'}")
print(f"n * q̂ = {n * q_hat:.2f} >= 5? {'Sim' if cond2 else 'Não'}")

# c) Valor crítico z_c e margem de erro E para 99% de confiança
conf_level = 0.99
alpha = 1 - conf_level
z_c = norm.ppf(1 - alpha/2)
E = z_c * math.sqrt((p_hat * q_hat) / n)
print(f"\nc) z_c (99%) = {z_c:.4f}")
print(f"   Margem de erro E = {E:.5f}")

# d) Intervalo de confiança
ic_inf = p_hat - E
ic_sup = p_hat + E
print(f"\nd) Intervalo de confiança 99% para a proporção:")
print(f"   ({ic_inf:.5f}, {ic_sup:.5f})")

# e) Interpretação
print("\ne) Interpretação:")
print(f"Com 99% de confiança, a proporção verdadeira de adultos que consideram")
print(f"pessoas acima de 65 anos como motoristas mais perigosos está entre {ic_inf:.4f} e {ic_sup:.4f}.")
print(f"A amostra foi suficientemente grande para usar a aproximação normal.")
