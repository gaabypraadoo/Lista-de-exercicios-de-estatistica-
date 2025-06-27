from scipy.stats import t
import math

# Dados
n = 36
df = n - 1
x_bar = 9.75
s = 2.39

# Função para calcular intervalo de confiança e margem de erro
def calcula_ic(nivel_confianca):
    alpha = 1 - nivel_confianca
    tc = t.ppf(1 - alpha/2, df)
    E = tc * (s / math.sqrt(n))
    inferior = x_bar - E
    superior = x_bar + E
    return tc, E, inferior, superior

# Calcula para 90% e 95%
tc_90, E_90, inf_90, sup_90 = calcula_ic(0.90)
tc_95, E_95, inf_95, sup_95 = calcula_ic(0.95)

# Mostra os resultados
print("Intervalo de Confiança 90%:")
print(f"t_c = {tc_90:.4f}")
print(f"Margem de erro (E) = {E_90:.4f}")
print(f"IC = ({inf_90:.4f}, {sup_90:.4f})\n")

print("Intervalo de Confiança 95%:")
print(f"t_c = {tc_95:.4f}")
print(f"Margem de erro (E) = {E_95:.4f}")
print(f"IC = ({inf_95:.4f}, {sup_95:.4f})\n")

print("Interpretação:")
print(f"O intervalo de confiança de 90% é mais estreito, refletindo menor margem de erro.")
print(f"O intervalo de confiança de 95% é mais amplo, pois exige maior certeza.")
print(f"Isso mostra que aumentar o nível de confiança aumenta a largura do intervalo,")
print(f"tornando a estimativa mais segura, porém menos precisa.")
