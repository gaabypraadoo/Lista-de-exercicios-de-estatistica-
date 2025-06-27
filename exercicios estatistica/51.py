# exercicio51.py
import scipy.stats as stats

# Dados do problema
alpha = 0.10
n = 9

# a. Graus de liberdade
gl = n - 1

# b. Valor crítico
t_critico = stats.t.ppf(1 - alpha, gl)

print("51. Valor crítico t para teste unilateral à direita:")
print(f"a. Graus de liberdade: {gl}")
print(f"b. Valor crítico t0: {t_critico:.4f}")
print(f"   Região de rejeição: t > {t_critico:.4f}")