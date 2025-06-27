from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Definindo os escores-z
z1 = -2.165
z2 = -1.35

# a) Desenhar a curva normal e sombrear a área entre z1 e z2
plt.figure(figsize=(10, 6))
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)

plt.plot(x, y, 'b-', label='Curva Normal Padrão (μ=0, σ=1)')
plt.fill_between(x, y, where=(x >= z1) & (x <= z2), color='red', alpha=0.3,
                label=f'Área entre z={z1:.3f} e z={z2:.2f}')

plt.axvline(z1, color='k', linestyle='--', label=f'z = {z1:.3f}')
plt.axvline(z2, color='k', linestyle=':', label=f'z = {z2:.2f}')
plt.axvline(0, color='g', linestyle='-', alpha=0.3, label='μ = 0')

plt.title('Área sob a Curva Normal Padrão entre z = -2.165 e z = -1.35')
plt.xlabel('Escore-z')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

# b) Encontrar a área à esquerda de z = -1.35
area_z2 = norm.cdf(z2)

# c) Encontrar a área à esquerda de z = -2.165
area_z1 = norm.cdf(z1)

# d) Subtrair as áreas para obter a área entre z1 e z2
area_between = area_z2 - area_z1

# Resultados
print("Resolução passo a passo:")
print(f"b) Área à esquerda de z = {z2:.2f}: {area_z2:.5f}")
print(f"c) Área à esquerda de z = {z1:.3f}: {area_z1:.5f}")
print(f"d) Área entre z1 e z2: {area_z2:.5f} - {area_z1:.5f} = {area_between:.5f}")

print("\nResposta final:")
print(f"A área sob a curva normal padrão entre z = {z1:.3f} e z = {z2:.2f} é: {area_between:.5f} ou {area_between*100:.2f}%")

# Interpretação
print("\nInterpretação:")
print(f"Esta área representa a probabilidade de um valor estar entre {z1:.3f} e {z2:.2f} desvios padrão abaixo da média")
print(f"Em uma distribuição normal padrão, aproximadamente {area_between*100:.2f}% dos valores estão neste intervalo")