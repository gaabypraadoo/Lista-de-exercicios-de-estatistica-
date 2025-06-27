from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Parâmetros fornecidos
mu = 129    # distância média de frenagem (pés)
sigma = 5.18 # desvio padrão (pés)
percentil = 0.01 # 1% mais baixo

# a) Esboçar um gráfico
plt.figure(figsize=(12, 6))
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

plt.plot(x, y, 'b-', label=f'Distribuição Normal (μ={mu}, σ={sigma:.2f})')
plt.fill_between(x, y, where=(x <= mu - 2*sigma), color='red', alpha=0.3,
                label='1% mais baixo')

plt.axvline(mu, color='green', linestyle='--', label='Média')
plt.title('Distribuição das Distâncias de Frenagem')
plt.xlabel('Distância de Frenagem (pés)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

# b) Encontrar o escore-z correspondente ao percentil 1%
z = norm.ppf(percentil)

# c) Calcular x usando a fórmula x = μ + zσ
x = mu + z * sigma

# Resultados
print("Resolução passo a passo:")
print(f"b) Escore-z para o 1º percentil (área acumulada = {percentil}):")
print(f"   z = {z:.4f}")

print(f"\nc) Cálculo da distância máxima:")
print(f"   x = μ + zσ = {mu} + ({z:.4f} × {sigma})")
print(f"   x = {x:.2f} pés")

# d) Interpretação do resultado
print("\nd) Interpretação:")
print(f"A maior distância de frenagem para um carro estar no grupo do 1% mais baixo é {x:.2f} pés.")
print(f"Isso significa que apenas 1% dos carros têm distâncias de frenagem menores que {x:.2f} pés.")
print(f"Valores abaixo de {x:.2f} pés são excepcionalmente bons (frenagens mais curtas).")

# Comparação com a regra empírica
print("\nComparação com a regra 68-95-99.7:")
print(f"1% mais baixo ≈ {mu - 2.33*sigma:.2f} pés (z ≈ -2.33)")
print(f"Nosso cálculo exato: {x:.2f} pés (z = {z:.4f})")