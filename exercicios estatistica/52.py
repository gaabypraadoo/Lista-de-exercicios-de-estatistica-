# exercicio52.py
import scipy.stats as stats

# Dados do problema
alpha = 0.05
n = 16

# a. Graus de liberdade
gl = n - 1

# b. Valores críticos
t_critico_pos = stats.t.ppf(1 - alpha/2, gl)
t_critico_neg = -t_critico_pos

print("52. Valores críticos t para teste bilateral:")
print(f"a. Graus de liberdade: {gl}")
print(f"b. Valores críticos: -t0 = {t_critico_neg:.4f}, t0 = {t_critico_pos:.4f}")
print(f"   Regiões de rejeição: t < {t_critico_neg:.4f} ou t > {t_critico_pos:.4f}")