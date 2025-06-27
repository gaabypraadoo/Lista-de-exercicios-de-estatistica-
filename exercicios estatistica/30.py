from scipy.stats import t
import math

# Dados
n = 16
df = n - 1
x_bar = 162.0
s = 10.0

# Função para calcular intervalo de confiança
def intervalo_confianca(nivel_confianca):
    alpha = 1 - nivel_confianca
    t_critico = t.ppf(1 - alpha/2, df)
    margem_erro = t_critico * (s / math.sqrt(n))
    inferior = x_bar - margem_erro
    superior = x_bar + margem_erro
    return inferior, superior

# Intervalos de confiança para 90% e 99%
ic_90 = intervalo_confianca(0.90)
ic_99 = intervalo_confianca(0.99)

print(f"Intervalo de confiança 90%: ({ic_90[0]:.2f}, {ic_90[1]:.2f}) ºF")
print(f"Intervalo de confiança 99%: ({ic_99[0]:.2f}, {ic_99[1]:.2f}) ºF")
