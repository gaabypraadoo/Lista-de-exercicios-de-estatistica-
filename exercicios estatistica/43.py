# exercicio43.py
import scipy.stats as stats

# Dados do problema
z = -1.71
alpha = 0.05

# a. Área correspondente a z = -1.71
p_value = stats.norm.cdf(z)

# c. Comparação com alpha
decisao = "Rejeitar H0" if p_value < alpha else "Não rejeitar H0"

print("43. Teste unilateral à esquerda com z = -1.71:")
print(f"a. Área correspondente (valor p): {p_value:.4f}")
print(f"c. Comparação: p-value = {p_value:.4f}, α = {alpha}")
print(f"   Decisão: {decisao} (pois {p_value:.4f} {'<' if p_value < alpha else '>='} {alpha})")