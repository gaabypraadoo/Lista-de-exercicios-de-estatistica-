# exercicio48.py
import scipy.stats as stats

# Dados do problema
alpha = 0.08

# a. Gráfico (conceitual)
print("48. Valores críticos para teste bilateral:")
print("a. Gráfico: Área de 0.04 em cada cauda da normal padrão")

# c. Escores-z críticos
z_critico_pos = stats.norm.ppf(1 - alpha/2)
z_critico_neg = stats.norm.ppf(alpha/2)

# d. Regiões de rejeição
print(f"\nc. Escores-z críticos: {z_critico_neg:.4f} e {z_critico_pos:.4f}")
print(f"\nd. Regiões de rejeição: z < {z_critico_neg:.4f} ou z > {z_critico_pos:.4f}")