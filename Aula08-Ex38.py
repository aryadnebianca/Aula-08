orcamento_disponivel = 1200.0
while orcamento_disponivel > 0:
    print(f"Saldo: R$ {orcamento_disponivel: .2f}")
    despesa = float(input("digite o valor da despesa: R$"))
    if despesa > orcamento_disponivel:
        print("Saldo insuficiente")
    else:
        orcamento_disponivel -= despesa
        print("f(Saldo final: {orcamento_disponivel: .2f}")



