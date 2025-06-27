# exercicio44.py
import scipy.stats as stats

# Dados do problema
z = 1.64
alpha = 0.10

# a. Área correspondente
area_cauda = 1 - stats.norm.cdf(z)
p_value = 2 * area_cauda

# c. Comparação com alpha
decisao = "Rejeitar H0" if p_value < alpha else "Não rejeitar H0"

print("44. Teste bilateral com z = 1.64:")
print(f"a. Área na cauda direita: {area_cauda:.4f}")
print(f"b. Valor p (bilateral): {p_value:.4f}")
print(f"c. Comparação: p-value = {p_value:.4f}, α = {alpha}")
print(f"   Decisão: {decisao} (pois {p_value:.4f} {'<' if p_value < alpha else '>='} {alpha})")