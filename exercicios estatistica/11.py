from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Função para plotar o percentil
def plot_percentil(percentil, p):
    z = norm.ppf(p)
    plt.figure(figsize=(10, 6))
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x)
    
    plt.plot(x, y, 'b-', label='Curva Normal Padrão')
    plt.fill_between(x, y, where=(x <= z), color='red', alpha=0.3,
                    label=f'Área acumulada = {p*100:.2f}%')
    
    plt.axvline(z, color='k', linestyle='--', label=f'{percentil} = z = {z:.3f}')
    plt.title(f'Escore-z para {percentil} (área acumulada = {p*100:.2f}%)')
    plt.xlabel('Escore-z')
    plt.ylabel('Densidade de Probabilidade')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return z

# 11.1 P10 (10º percentil)
p10 = 0.10
z_p10 = plot_percentil("P10", p10)

# 11.2 P20 (20º percentil)
p20 = 0.20
z_p20 = plot_percentil("P20", p20)

# 11.3 P99 (99º percentil)
p99 = 0.99
z_p99 = plot_percentil("P99", p99)

# Resultados
print("Respostas:")
print(f"11.1 P10: z = {z_p10:.3f}")
print(f"11.2 P20: z = {z_p20:.3f}")
print(f"11.3 P99: z = {z_p99:.3f}")

# Explicação adicional
print("\nMétodo de cálculo:")
print("1. Convertemos o percentil para área acumulada (P10 = 0.10, P20 = 0.20, etc.)")
print("2. Usamos a função percentil (norm.ppf) para encontrar o escore-z correspondente")
print("3. Para percentis altos (como P99), o escore-z será positivo")
print("4. Para percentis baixos (como P10), o escore-z será negativo")