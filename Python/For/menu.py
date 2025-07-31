print("Monte um sistema que repita um menu até o usuário escolher sair. Use while e break.")
opcao = 0

while opcao != 4:
    print("Menu: ")
    print("1 - opção 1")
    print("2 - opção 2")
    print("3 - opção 3")
    print("4 - sair")

    opcao = int(input("Escolha uma opção: \n"))

    if opcao == 1:
        print("Você escolheu a opção 1.")
    elif opcao == 2:
        print("Você escolheu a opção 2")
    elif opcao == 3:
        print("Você escolheu a opção 3")
    elif opcao == 4:
        print("Saindo...")
        break  # Encerra o loop quando a opção 4 é escolhida
    else:
        print("Opção inválida, tente novamente.")
