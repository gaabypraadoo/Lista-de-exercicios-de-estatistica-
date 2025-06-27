# exercicio53.py
import scipy.stats as stats

# Dados do problema
mu0 = 1200
x_bar = 1125
s = 55
n = 7
alpha = 0.10

# a. Formulação de hipóteses
print("53. Teste t para custo de seguro:")
print(f"a. Afirmação: μ < {mu0}")
print(f"   H0: μ >= {mu0}, Ha: μ < {mu0}")

# b. Graus de liberdade e significância
gl = n - 1
print(f"\nb. α = {alpha}, gl = {gl}")

# c. Valor crítico e região de rejeição
t_critico = stats.t.ppf(alpha, gl)
print(f"\nc. Valor crítico: {t_critico:.4f}")
print(f"   Região de rejeição: t < {t_critico:.4f}")

# d. Estatística de teste
t = (x_bar - mu0) / (s / (n**0.5))
print(f"\nd. Estatística de teste: t = {t:.4f}")

# e. Decisão
decisao = "Rejeitar H0" if t < t_critico else "Não rejeitar H0"
print(f"\ne. Decisão: {decisao}")

# f. Interpretação
print(f"\nf. Interpretação: {decisao} a afirmação do agente ao nível de")
print(f"   significância de {alpha*100}%")