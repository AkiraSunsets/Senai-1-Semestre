num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")

elif operacao == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")

elif operacao == "*":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Divisão por zero não é permitida!")

else:
    print("Operação inválida!")
