import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Vamos criar três curvas normais para análise
# Como a figura não foi fornecida, farei suposições razoáveis sobre as médias e desvios padrão

# Curva A: média 0, desvio padrão 1
# Curva B: média 2, desvio padrão 1.5
# Curva C: média -1, desvio padrão 0.8

# Parâmetros das curvas
mu_A, sigma_A = 0, 1
mu_B, sigma_B = 2, 1.5
mu_C, sigma_C = -1, 0.8

# Criando pontos para o eixo x
x = np.linspace(-5, 5, 1000)

# Calculando as PDFs (Probability Density Functions)
pdf_A = norm.pdf(x, mu_A, sigma_A)
pdf_B = norm.pdf(x, mu_B, sigma_B)
pdf_C = norm.pdf(x, mu_C, sigma_C)

# Plotando as curvas
plt.figure(figsize=(10, 6))
plt.plot(x, pdf_A, 'b-', label=f'Curva A: μ={mu_A}, σ={sigma_A}')
plt.plot(x, pdf_B, 'r--', label=f'Curva B: μ={mu_B}, σ={sigma_B}')
plt.plot(x, pdf_C, 'g:', label=f'Curva C: μ={mu_C}, σ={sigma_C}')

# Adicionando linhas de simetria (médias)
plt.axvline(mu_A, color='b', linestyle=':', alpha=0.5)
plt.axvline(mu_B, color='r', linestyle=':', alpha=0.5)
plt.axvline(mu_C, color='g', linestyle=':', alpha=0.5)

plt.title('Comparação de Curvas Normais')
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

# Respondendo às perguntas do exercício
print("\nRespostas:")
print("a) A linha de simetria de cada curva (sua média) está em:")
print(f"   Curva A: μ = {mu_A}")
print(f"   Curva B: μ = {mu_B}")
print(f"   Curva C: μ = {mu_C}")
print(f"   Conclusão: A curva com a média maior é a Curva B (μ = {mu_B})")

print("\nb) A dispersão de cada curva pode ser observada pela largura:")
print(f"   Curva A: σ = {sigma_A}")
print(f"   Curva B: σ = {sigma_B}")
print(f"   Curva C: σ = {sigma_C}")
print(f"   Conclusão: A curva com o desvio padrão maior é a Curva B (σ = {sigma_B})")