quantidade_vendas = 0
continuar = "sim"
while continuar == "sim":
    quantidade_vendas += 1
    continuar = input("deseja adicionar outra venda?: ")
    print(f"quantidade de vendas é igual a: {quantidade_vendas}")
