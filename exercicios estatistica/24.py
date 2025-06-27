# Dados extraídos da imagem (28 valores)
horas = [
    26, 25, 32, 31, 28,
    28, 22, 28, 25, 21, 40,
    32, 22, 25, 22, 24,
    46, 20, 35, 32, 22, 48,
    32, 36, 38, 32, 22, 19
]

# a. Média amostral
media_amostral = sum(horas) / len(horas)
print(f"a. Média amostral (x̄) = {media_amostral:.2f}")

# b. Estimativa pontual para μ (média populacional)
# É a própria média amostral
print(f"b. Estimativa pontual da média populacional (μ̂) = {media_amostral:.2f}")
