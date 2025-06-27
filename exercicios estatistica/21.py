import math
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# a. Verificar se pode usar distribuição normal
n = 100
p = 0.34
q = 1 - p

np_ = n * p
nq = n * q

usa_normal = np_ >= 5 and nq >= 5

print(f"a. Pode usar aproximação normal? {usa_normal} (np = {np_:.2f}, nq = {nq:.2f})")

# b. Média e desvio padrão
mu = np_
sigma = math.sqrt(n * p * q)
print(f"b. Média (μ) = {mu:.2f}, Desvio padrão (σ) = {sigma:.2f}")

# c. Correção de continuidade: P(x > 30) -> P(x > 30.5)
x_corrigido = 30.5

# d. Escore Z
z = (x_corrigido - mu) / sigma
print(f"d. Escore-z para x = 30.5: z = {z:.2f}")

# e. Área à esquerda de z (P(X <= 30.5)), queremos P(X > 30.5) = 1 - P(Z <= z)
prob = 1 - norm.cdf(z)
print(f"e. P(x > 30) ≈ P(z > {z:.2f}) = {prob:.4f} ({prob*100:.2f}%)")

# --- Gráfico (opcional) ---
# Distribuição normal aproximada
x_vals = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y_vals = norm.pdf(x_vals, mu, sigma)

plt.figure(figsize=(10,5))
plt.plot(x_vals, y_vals, label='Distribuição Normal')
plt.fill_between(x_vals, y_vals, where=(x_vals > x_corrigido), color='orange', alpha=0.5, label='Área: P(X > 30)')
plt.axvline(x_corrigido, color='red', linestyle='--', label='Correção de continuidade: 30.5')
plt.title('Aproximação Normal para P(X > 30)')
plt.xlabel('Número de pessoas que responderam "sim"')
plt.ylabel('Densidade de probabilidade')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
