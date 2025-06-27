# exercicio47.py
import scipy.stats as stats

# Dados do problema
alpha = 0.10

# a. Gráfico (conceitual)
print("47. Valor crítico para teste unilateral à esquerda:")
print("a. Gráfico: Área de 0.10 na cauda esquerda da normal padrão")

# c. Escore-z crítico
z_critico = stats.norm.ppf(alpha)

# d. Região de rejeição
print(f"\nc. Escore-z crítico: {z_critico:.4f}")
print(f"\nd. Região de rejeição: z < {z_critico:.4f}")