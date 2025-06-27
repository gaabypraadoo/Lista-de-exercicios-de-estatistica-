# exercicio37.py
import scipy.stats as stats
import math

# Dados do problema
n = 30
s = 1.20  # desvio padrão amostral
confiancas = [0.90, 0.95]

print("37. Intervalos de confiança para variância e desvio padrão:")
print(f"Tamanho da amostra: {n}, Desvio padrão amostral: {s} mg\n")

for confianca in confiancas:
    alpha = 1 - confianca
    gl = n - 1
    
    # a. Valores críticos χ²
    chi2_R = stats.chi2.ppf(1 - alpha/2, gl)
    chi2_L = stats.chi2.ppf(alpha/2, gl)
    
    # b. Limites para variância
    var_amostral = s**2
    limite_inf_var = ((n - 1) * var_amostral) / chi2_R
    limite_sup_var = ((n - 1) * var_amostral) / chi2_L
    
    # c. Limites para desvio padrão
    limite_inf_dp = math.sqrt(limite_inf_var)
    limite_sup_dp = math.sqrt(limite_sup_var)
    
    print(f"Para {confianca*100}% de confiança:")
    print(f"a. Valores críticos: χ²_R = {chi2_R:.4f}, χ²_L = {chi2_L:.4f}")
    print(f"b. Intervalo para variância: ({limite_inf_var:.4f}, {limite_sup_var:.4f})")
    print(f"c. Intervalo para desvio padrão: ({limite_inf_dp:.4f}, {limite_sup_dp:.4f})")
    print()