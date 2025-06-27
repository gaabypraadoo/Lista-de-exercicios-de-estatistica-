# exercicio46.py
import scipy.stats as stats

# Dados do problema
mu0 = 3
x_bar = 3.3
sigma = 0.5
n = 25
alpha = 0.01

# a. Formulação de hipóteses
print("46. Teste para tempo de recuperação:")
print(f"a. Afirmação do estudo: μ = {mu0} anos")
print(f"   H0: μ = {mu0}, Ha: μ ≠ {mu0}")

# b. Nível de significância
print(f"\nb. α = {alpha}")

# c. Estatística de teste
z = (x_bar - mu0) / (sigma / (n**0.5))
print(f"\nc. Estatística de teste: z = {z:.4f}")

# d. Valor p (bilateral)
p_value = 2 * (1 - stats.norm.cdf(abs(z)))
print(f"\nd. Valor p: {p_value:.4f}")

# e. Decisão
decisao = "Rejeitar H0" if p_value < alpha else "Não rejeitar H0"
print(f"\ne. Decisão: {decisao}")

# f. Interpretação
print(f"\nf. Interpretação: {decisao} a afirmação do estudo ao nível de")
print(f"   significância de {alpha*100}%")