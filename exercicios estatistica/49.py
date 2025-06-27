# exercicio49.py
import scipy.stats as stats

print("49. Testes para afirmações da companhia:")

# Primeiro teste: Salário
mu0_salario = 68000
x_bar_salario = 66900
sigma_salario = 5500
n_salario = 20
alpha_salario = 0.05

print("\n1. Teste para salário médio:")
print(f"Afirmação: μ < {mu0_salario}")
print(f"H0: μ >= {mu0_salario}, Ha: μ < {mu0_salario}")

z_salario = (x_bar_salario - mu0_salario) / (sigma_salario / (n_salario**0.5))
p_value_salario = stats.norm.cdf(z_salario)

print(f"Estatística de teste: z = {z_salario:.4f}")
print(f"Valor p: {p_value_salario:.4f}")

decisao_salario = "Rejeitar H0" if p_value_salario < alpha_salario else "Não rejeitar H0"
print(f"Decisão: {decisao_salario}")

# Segundo teste: Jornada
mu0_jornada = 8.5
x_bar_jornada = 8.2
sigma_jornada = 0.5
n_jornada = 25
alpha_jornada = 0.01

print("\n2. Teste para jornada média:")
print(f"Afirmação: μ < {mu0_jornada}")
print(f"H0: μ >= {mu0_jornada}, Ha: μ < {mu0_jornada}")

z_jornada = (x_bar_jornada - mu0_jornada) / (sigma_jornada / (n_jornada**0.5))
p_value_jornada = stats.norm.cdf(z_jornada)

print(f"Estatística de teste: z = {z_jornada:.4f}")
print(f"Valor p: {p_value_jornada:.4f}")

decisao_jornada = "Rejeitar H0" if p_value_jornada < alpha_jornada else "Não rejeitar H0"
print(f"Decisão: {decisao_jornada}")