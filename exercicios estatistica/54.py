# exercicio54.py
import scipy.stats as stats

print("54. Testes t para afirmações da indústria:")

# Primeiro teste: pH
mu0_ph = 6.8
x_bar_ph = 6.7
s_ph = 0.35
n_ph = 39
alpha_ph = 0.05

print("\n1. Teste para pH da água:")
print(f"Afirmação: μ = {mu0_ph}")
print(f"H0: μ = {mu0_ph}, Ha: μ ≠ {mu0_ph}")

gl_ph = n_ph - 1
t_ph = (x_bar_ph - mu0_ph) / (s_ph / (n_ph**0.5))
p_value_ph = 2 * (1 - stats.t.cdf(abs(t_ph), gl_ph))

print(f"Estatística de teste: t = {t_ph:.4f}")
print(f"Valor p: {p_value_ph:.4f}")

decisao_ph = "Rejeitar H0" if p_value_ph < alpha_ph else "Não rejeitar H0"
print(f"Decisão: {decisao_ph}")

# Segundo teste: Condutividade
mu0_cond = 1890
x_bar_cond = 2350
s_cond = 900
n_cond = 39
alpha_cond = 0.01

print("\n2. Teste para condutividade:")
print(f"Afirmação: μ = {mu0_cond}")
print(f"H0: μ = {mu0_cond}, Ha: μ ≠ {mu0_cond}")

gl_cond = n_cond - 1
t_cond = (x_bar_cond - mu0_cond) / (s_cond / (n_cond**0.5))
p_value_cond = 2 * (1 - stats.t.cdf(abs(t_cond), gl_cond))

print(f"Estatística de teste: t = {t_cond:.4f}")
print(f"Valor p: {p_value_cond:.4f}")

decisao_cond = "Rejeitar H0" if p_value_cond < alpha_cond else "Não rejeitar H0"
print(f"Decisão: {decisao_cond}")