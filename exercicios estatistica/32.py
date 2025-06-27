n = 18
s = 2.5
conf_level = 0.90
pop_normal = True
sigma_desconhecido = True  # Só temos s, não sigma

if n >= 30 and not sigma_desconhecido:
    dist = "normal padrão (z)"
elif n < 30 and sigma_desconhecido and pop_normal:
    dist = "distribuição t de Student"
else:
    dist = "nenhuma delas (precisa de outro método)"

print(f"Com n = {n}, desvio padrão populacional desconhecido e população normal,")
print(f"devemos usar a {dist} para construir o intervalo de confiança de {conf_level*100:.0f}%")
