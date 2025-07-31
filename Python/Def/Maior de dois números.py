print("O maior de dois números")

def maior(num1,num2):
    if num2 > num1:
        return num2
    else:
        return num1

num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))

calculo = maior(num1,num2)

print(f"O maior número entre {num1} e {num2} é {calculo}")
