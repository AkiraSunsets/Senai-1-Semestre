n = int(input("Digite o tamanho da lista: "))
numeros = []
soma = 0
for _ in range(n):
    numero = float(input("Digite um número: "))
    numeros.append(numero)
    soma = soma + numero
    media = soma / n
    print("A média dos números é:", media)

x = 1
y = 2
z = 0
for i in range(3):
z = z + x
x = x + y
print(x, y, z)

x = 0
while x <= 3:
    print(x)
x = x + 1


m = 5
n = 1
while m > 2:
    n = n + 2
    m = m - 1
    print(m,n)


#peça que o usuario digite um número de 5 a 10 e exiba a contagem regressiva
contador = int(input("Digite um número entre 5 e 10: "))
while contador > 0:
    print(contador)
    contador -= 1
    #contador = contador -1

#escreva um programa que peça ao usuario 5 numeros e exiba o maior deles usando loop while

maior = float(0.0)

contador = 1
while contador <= 5:
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
        contador += 1
print("O maior número é:",maior)



#crie um programa que calcule o fatorial de um número dado pelo usuário usando o loop while
numero = int(input("Digite um número inteiro: \n"))
fatorial = 1
i = 1

while i <= numero:
    fatorial *=1
    i += 1
print("O resultado de", numero, "é", fatorial)

#Faça um programa que exiba a média de uma lista de números(tamanho da lista é definido
#pelo usuário) usando while

n = int(input("Digite um número: \n"))
numeros = []
contador = 0
while contador < n:
    numero = float(input("Digite um número: "))
    numeros.append(numero)
    contador += 1
media = sum(numeros)/n
print("A média dos números é:", media)

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

while True:
    resposta = input("Digite sair para encerrar: ")
    if resposta == 'sair':
        break


for i in range(5):
    if i == 2:
        continue
    print(i)
