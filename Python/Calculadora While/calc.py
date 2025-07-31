#calculadora com menu

opcao = 0

while opcao != 5:
    print("Menu: ")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print("Resultado:", resultado)

    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print("Resultado:", resultado)

    elif opcao == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print("Resultado:", resultado)

    elif opcao == 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if num2 == 0:
            print("Erro: Divisão por zero")
        else:
            resultado = num1 / num2
            print("Resultado:", resultado)

    elif opcao == 5:
        print("Saindo...")

    else:
        print("Opção inválida! Tente novamente.")
