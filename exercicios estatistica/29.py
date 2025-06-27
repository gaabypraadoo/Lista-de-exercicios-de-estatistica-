from scipy.stats import t

# Dados
n = 22
df = n - 1         # graus de liberdade
conf_level = 0.90  # nível de confiança

alpha = 1 - conf_level
# t crítico (para duas caudas, então usamos 1 - alpha/2)
tc = t.ppf(1 - alpha/2, df)

print(f"a) Graus de liberdade (df): {df}")
print(f"b) Nível de confiança (c): {conf_level*100:.0f}%")
print(f"c) Valor crítico t_c: {tc:.4f}")

print("\nd) Interpretação:")
print(f"O valor crítico t_c = {tc:.4f} é o ponto na distribuição t de Student com {df} graus de liberdade,")
print(f"que delimita as regiões de rejeição para um intervalo de confiança de {conf_level*100:.0f}%.")
print("Isso significa que, para construir um intervalo de confiança bilateral de 90%,")
print(f"usamos t_c para determinar a amplitude do intervalo em torno da média amostral.")
