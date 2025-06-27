import math
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Dados
n = 180           # total de adultos (ajuste se for outro valor)
p = 0.58          # proporção que não usa capacete
q = 1 - p
x = 100           # queremos P(X <= 100)

# a. Verificar se pode usar normal
np_ = n * p
nq = n * q
usa_normal = np_ >= 5 and nq >= 5
print(f"a. Pode usar aproximação normal? {usa_normal} (np = {np_:.2f}, nq = {nq:.2f})")

# b. Calcular média e desvio padrão
mu = np_
sigma = math.sqrt(n * p * q)
print(f"b. Média (μ) = {mu:.2f}, Desvio padrão (σ) = {sigma:.2f}")

# c. Correção de continuidade: P(X <= 100) -> P(X <= 100.5)
x_corrigido = 100.5

# d. Escore-z
z = (x_corrigido - mu) / sigma
print(f"d. Escore-z para x = 100.5: z = {z:.2f}")

# e. Calcular probabilidade P(X <= 100.5) = P(Z <= z)
prob = norm.cdf(z)
print(f"e. P(X ≤ 100) ≈ P(Z ≤ {z:.2f}) = {prob:.4f} ({prob*100:.2f}%)")

# --- Gráfico (opcional) ---
x_vals = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y_vals = norm.pdf(x_vals, mu, sigma)

plt.figure(figsize=(10,5))
plt.plot(x_vals, y_vals, label='Distribuição Normal')
plt.fill_between(x_vals, y_vals, where=(x_vals <= x_corrigido), color='skyblue', alpha=0.5, label='Área: P(X ≤ 100)')
plt.axvline(x_corrigido, color='red', linestyle='--', label='Correção de continuidade: 100.5')
plt.title('Aproximação Normal para P(X ≤ 100)')
plt.xlabel('Número de adultos que não usam capacete')
plt.ylabel('Densidade de probabilidade')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()