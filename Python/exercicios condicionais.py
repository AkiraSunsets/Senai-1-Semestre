n = int(input("Insira um número: "))
if n < 12:
    print("criança")

elif n < 18:
    print("adolescente")

elif n < 65:
    print("adulto")


n = int(input("Insira sua idade: "))
if n < 18:
    print("Você é menor de idade")

elif n < 65:
    print("Você é maior de idade")



n = float(input("Insira sua nota: "))

if n > 9:
    print("Excelente")

elif n >= 7.0 and n < 9.0:
    print("Média")

elif n < 5.0:
    print("Nota insuficiente")

else:
    print("Nota fora do intervalo")


num = int(input("Insira um número: "))

if num % 2 != 0:
    print("Impar")

elif num % 2 == 0:
    print("par")

if (num % 3 == 0) or (num % 5 == 0):
    print("Divisivel por 3 ou 5")

else:
    print("Não é divisivel por 3 nem por 5")


num1 = int(input("Insira um número: "))
num2 = int(input("Insira um número: "))

if num1 > num2:
    print("Num1 é maior que num2")

elif num1 < num2:
    print("Num2 é maior que num1")

else:
    print("Os números são iguais")

num = int(input("Insira um número: "))
if num < 2:
    print("bebê")

elif num < 13:
    print("criança")

elif num < 18:
    print("adolescente")

elif num < 60:
    print("adulto")

elif num >= 60:
    print("idoso")

else:
    print("")

opcao = input("Escolha a conversão(C para Celsius para Fahrenheit):").upper()
valor = float(input("Digite o valor da temperatura: "))

if opcao == "C":
   temperatura_fahrenheit = (valor * 9/5) + 32
   print("A temperatura em Fahrenheit é:", temperatura_fahrenheit)
elif opcao == "F":
   temperatura_celsius = (valor - 32) * 5/9
   print("A temperatura em Celsius é:", temperatura_celsius)
else:
   print("Opção inválida")

a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))

# Testando se é triângulo
if (a + b < c) or (a + c < b) or (b + c < a):
   print('Nao é um triangulo')
elif (a == b) and (a == c):
   print('Equilatero')
elif (a == b) or (a == c) or (b == c):
   print('Isósceles')
else:
   print('Escaleno')

#Estrutura de decisão

idade = int(input("Insira sua idade: "))
renda = float(input("Insira sua renda: "))

if idade > 18:
    print("Qualificado para emitir um empréstimo")
elif idade < 18:
    if renda > 1000:
        print("Pode pedir empréstimo se tiver renda acima de R$ 1.000,00")
    else:
        print("Não pode pedir empréstimo")
elif idade >= 18:
    if renda > 1500:
        print("Pode pedir um empréstimo")
    else:
        print("Não pode pedir um empréstimo")







