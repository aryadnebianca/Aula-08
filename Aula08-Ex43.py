print("1 - Vendas")
print("2 - Recursos Humanos")
print("3 - Financeiro")
opcao_menu = int(input("Digite qual área deseja escolher: "))
match opcao_menu:
    case 1:
        print("Abrindo relatório de Vendas")
    case 2:
        print("Abrindo relatório de Recursos Humanos")
    case 3:
        print("Abrindo relatório de Finanças")
    case _:
        print("Opção inválida")