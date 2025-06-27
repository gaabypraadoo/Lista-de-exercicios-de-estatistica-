# exercicio39.py
print("39. Teste de hipótese para taxa de falha de paraquedas:")

# a. Formulação de hipóteses
print("a. H0: p ≤ 0.01 (a taxa de falha é no máximo 1%) - afirmação da empresa")
print("   Ha: p > 0.01 (a taxa de falha é maior que 1%)")

# b. Erros possíveis
print("\nb. Erro Tipo I: Rejeitar H0 quando é verdadeira (concluir que a taxa é >1% quando na verdade não é)")
print("   Erro Tipo II: Não rejeitar H0 quando é falsa (aceitar que a taxa é ≤1% quando na verdade é maior)")

# c. Qual erro é mais grave
print("\nc. O erro Tipo II é mais grave, pois significaria aceitar paraquedas com taxa de falha maior que o declarado,")
print("   colocando os usuários em risco. O erro Tipo I seria apenas uma acusação injusta à empresa.")