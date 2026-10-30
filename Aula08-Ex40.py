faturamento_mensal = 0
for dia in range(1, 31):
    venda_do_dia = float(input("Vendas do dia {dia}: R$"))
    faturamento_mensal += venda_do_dia
media_mensal = faturamento_mensal/30
print(f"Faturamento mensal: R${faturamento_mensal:.2f}")
print(f"Média mensal: {media_mensal: .2f}")
