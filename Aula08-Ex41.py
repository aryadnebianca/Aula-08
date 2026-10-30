for numero_venda in range(1, 6):
    valor_venda = float(input(f"Valor da venda {numero_venda}: R$"))
    if valor_venda > 500:
        classificacao = "supera"
    else:
        classificacao = "não supera"
print(f"venda {numero_venda}: {classificacao}")
