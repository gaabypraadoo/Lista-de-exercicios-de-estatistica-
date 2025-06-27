from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# 10.1: Escore-z com 96.16% da área à direita
area_direita = 0.9616
area_esquerda = 1 - area_direita

# Encontrar o escore-z correspondente
z_10_1 = norm.ppf(area_esquerda)  # Função percentil (inversa da CDF)

# Visualização
plt.figure(figsize=(10, 6))
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)

plt.plot(x, y, 'b-', label='Curva Normal Padrão')
plt.fill_between(x, y, where=(x >= z_10_1), color='red', alpha=0.3,
                label=f'Área à direita = {area_direita*100:.2f}%')

plt.axvline(z_10_1, color='k', linestyle='--', label=f'z = {z_10_1:.3f}')
plt.title(f'Escore-z com {area_direita*100:.2f}% da área à direita')
plt.xlabel('Escore-z')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

print("Resolução 10.1:")
print(f"Área à esquerda desejada: 1 - {area_direita} = {area_esquerda}")
print(f"Escore-z correspondente: {z_10_1:.3f}")

# 10.2: Escore-z com 95% da área entre -z e z
area_central = 0.95
area_caudas = 1 - area_central
area_esquerda = area_caudas / 2

# Encontrar o escore-z correspondente
z_10_2 = norm.ppf(1 - area_esquerda)  # z positivo

# Visualização
plt.figure(figsize=(10, 6))
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)

plt.plot(x, y, 'b-', label='Curva Normal Padrão')
plt.fill_between(x, y, where=(x >= -z_10_2) & (x <= z_10_2), color='green', alpha=0.3,
                label=f'Área central = {area_central*100:.2f}%')

plt.axvline(-z_10_2, color='k', linestyle='--', label=f'-z = {-z_10_2:.3f}')
plt.axvline(z_10_2, color='k', linestyle='--', label=f'z = {z_10_2:.3f}')
plt.title(f'Escore-z com {area_central*100:.2f}% da área entre -z e z')
plt.xlabel('Escore-z')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

print("\nResolução 10.2:")
print(f"Área nas caudas: 1 - {area_central} = {area_caudas}")
print(f"Área em cada cauda: {area_caudas} / 2 = {area_esquerda}")
print(f"Escore-z positivo correspondente: {z_10_2:.3f}")
print(f"Intervalo: [{-z_10_2:.3f}, {z_10_2:.3f}]")