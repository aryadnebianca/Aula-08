meta_mensal = 2000
for numero_funcionario in range(1, 5):
    nome_funcionario = input("digite seu nome: ")
    vendas_mensais = float(input("digite o total das suas vendas: "))
    if vendas_mensais > meta_mensal:
        comissao = vendas_mensais * 0.08
    else:
        comissao = 0
print(f"{nome_funcionario}: comissão de R$ {comissao:.2f}")