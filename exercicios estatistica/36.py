# exercicio36.py
import scipy.stats as stats

# Dados do problema
n = 30
confianca = 0.90

# a. Graus de liberdade e nível de confiança
graus_liberdade = n - 1
alpha = 1 - confianca

# b. Áreas à direita de χ²_R e χ²_L
area_chi2_R = alpha / 2
area_chi2_L = 1 - (alpha / 2)

# c. Encontrar χ²_R e χ²_L usando a tabela de distribuição chi-quadrado
chi2_R = stats.chi2.ppf(area_chi2_L, graus_liberdade)
chi2_L = stats.chi2.ppf(area_chi2_R, graus_liberdade)

# d. Interpretação
print(f"36. Valores críticos para IC de {confianca*100}% com n={n}:")
print(f"a. Graus de liberdade: {graus_liberdade}, Nível de confiança: {confianca}")
print(f"b. Área à direita de χ²_R: {area_chi2_R:.4f}, Área à direita de χ²_L: {1-area_chi2_L:.4f}")
print(f"c. Valores críticos: χ²_R = {chi2_R:.4f}, χ²_L = {chi2_L:.4f}")
print("d. Interpretação: Estes valores delimitam o intervalo onde a variância populacional está com 90% de confiança.")