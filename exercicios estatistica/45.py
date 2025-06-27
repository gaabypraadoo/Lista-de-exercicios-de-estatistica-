# exercicio45.py
import scipy.stats as stats

# Dados do problema
mu0 = 35
x_bar = 36
sigma = 4
n = 100
alpha = 0.05

# a. Formulação de hipóteses
print("45. Teste para velocidade média de veículos:")
print(f"a. Afirmação: μ > {mu0} mph")
print(f"   H0: μ <= {mu0}, Ha: μ > {mu0}")

# b. Nível de significância
print(f"\nb. α = {alpha}")

# c. Estatística de teste
z = (x_bar - mu0) / (sigma / (n**0.5))
print(f"\nc. Estatística de teste: z = {z:.4f}")

# d. Valor p
p_value = 1 - stats.norm.cdf(z)
print(f"\nd. Valor p: {p_value:.4f}")

# e. Decisão
decisao = "Rejeitar H0" if p_value < alpha else "Não rejeitar H0"
print(f"\ne. Decisão: {decisao}")

# f. Interpretação
print(f"\nf. Interpretação: {decisao} que a velocidade média é maior que {mu0} mph")
print(f"   ao nível de significância de {alpha*100}%")