import math

# a. Identificar os parâmetros
n = 100         # número de tentativas
p = 0.34        # probabilidade de sucesso ("sim")
q = 1 - p       # probabilidade de fracasso ("não")

# b. Calcular np e nq
np_ = n * p
nq = n * q

# c. Verificar se pode usar aproximação normal
usa_normal = np_ >= 5 and nq >= 5

# d. Calcular média e desvio padrão se for apropriado
if usa_normal:
    mu = np_
    sigma = math.sqrt(n * p * q)
    print(f"É possível usar aproximação normal")
    print(f"Média (μ) = {mu:.2f}")
    print(f"Desvio padrão (σ) = {sigma:.2f}")
else:
    print("Não é possível usar aproximação normal.")
    print(f"np = {np_:.2f}, nq = {nq:.2f} (precisam ser ambos ≥ 5)")
