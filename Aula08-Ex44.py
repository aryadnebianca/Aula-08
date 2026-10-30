print("1 - Troca")
print("2 - Devolução")
print("3 - Suporte")
opcao_escolhida = int(input("Digite qual a opção desejada: "))
match opcao_escolhida:
    case 1:
        print("Solicitando troca")
    case 2:
        print("Solicitando devolução")
    case 3:
        print("Solicitando atendimento")
    case _:
        print("Opção inválida")