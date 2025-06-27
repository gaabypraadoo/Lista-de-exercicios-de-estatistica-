# exercicio50.py
import scipy.stats as stats

# Dados do problema
mu0 = 13960
x_bar = 13725
sigma = 2345
n = 500
alphas = [0.10, 0.01]

print("50. Teste para custo médio de criação de filhos:")

for alpha in alphas:
    print(f"\nPara α = {alpha}:")
    
    # b. Valores críticos
    z_critico_neg = stats.norm.ppf(alpha/2)
    z_critico_pos = stats.norm.ppf(1 - alpha/2)
    
    # c. Estatística de teste
    z = (x_bar - mu0) / (sigma / (n**0.5))
    
    # Decisão
    if z < z_critico_neg or z > z_critico_pos:
        decisao = "Rejeitar H0"
    else:
        decisao = "Não rejeitar H0"
    
    print(f"b. Valores críticos: {z_critico_neg:.4f} e {z_critico_pos:.4f}")
    print(f"   Estatística de teste: z = {z:.4f}")
    print(f"c. Decisão: {decisao}")
    print(f"d. Interpretação: {decisao} a afirmação de que o custo médio é ${mu0}")