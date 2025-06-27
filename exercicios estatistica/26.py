import math
from scipy.stats import norm

# Dados (extraídos do exercício 24)
horas = [
    26, 25, 32, 31, 28,
    28, 22, 28, 25, 21, 40,
    32, 22, 25, 22, 24,
    46, 20, 35, 32, 22, 48,
    32, 36, 38, 32, 22, 19
]

# a. Calcular x̄ e E
n = len(horas)
x_barra = sum(horas) / n
sigma = 7.9
zc = norm.ppf(0.975)  # nível de confiança de 95%

E = zc * (sigma / math.sqrt(n))

# b. Limites do intervalo de confiança
limite_inferior = x_barra - E
limite_superior = x_barra + E

# Resultados
print(f"a. x̄ (média amostral) = {x_barra:.2f}")
print(f"   E (margem de erro) = {E:.2f}")
print(f"b. Intervalo de confiança de 95%: ({limite_inferior:.2f}, {limite_superior:.2f})")
print("c. Interpretação: Com 95% de confiança, a média real de horas semanais trabalhadas")
print(f"   está entre {limite_inferior:.2f} e {limite_superior:.2f} horas.")
