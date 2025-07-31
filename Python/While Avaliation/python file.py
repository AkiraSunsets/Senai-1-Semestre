#Peça 10 números e conte quantos são múltiplos de 3. Use for.
contador = 0
for num in range(10):
    int = input("Digite um número: \n")
    if num %3 == 0:
        contador += 1
        print("Multiplo de 3")
    else:
        print("Não é multiplo de 3")

print(f"A quantidade de números múltiplos de 3 é: {contador} ")
---------------------------------------------------------------------------------------------------------------------
#2) Crie um programa que simule o uso de senha com tentativas infinitas até digitar a senha correta (use while True).
senha_correta = "1234"

while True: #loop infinito até encontrar a senha correta.
    senha = input("Digite a senha: \n")

    if senha == senha_correta:
        print("Senha correta!")
        break  # encerra o loop quando a senha estiver correta.
    else:
        print("Senha incorreta, tente novamente.")
---------------------------------------------------------------------------------------------------------------------
#3)Monte um sistema que repita um menu até o usuário escolher sair. Use while e break.
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

----------------------------------------------------------------------------------------------
# Crie um programa que peça dois números inteiros
# e exiba todos os números entre eles que são primos.
# Use for
num_first = int(input("Digite o primeiro número: \n"))
num_second = int(input("Digite o segundo número: \n"))

print(f"Números primos entre {num_first} e {num_second}:")

for numero in range(num_first, num_second + 1):
    if numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                break
        else:
            print(numero)
---------------------------------------------------------------------------------------------
#5) O usuário tem 3 tentativas para acertar a senha.
# Se errar todas, o acesso é bloqueado. Use while.
senha = 1234
contador = 0

while contador < 3:
    senha_correta = int(input("Insira sua senha: "))
    if senha == senha_correta:
        print("Welcome!")
        break
    else:
        contador += 1
        if contador == 3:
            print("Acesso restrito")
            break
-----------------------------------------------------------------------------------------
#6) Peça 10 números e separe em duas listas: pares e ímpares. Mostre as duas no final.
# Inicializando as listas de pares e ímpares
pares = []
impares = []

# Laço para solicitar 10 números
for num in range(10):
    number = int(input("Digite um número: \n"))
    if number % 2 == 0:
        pares.append(number)
    else:
        impares.append(number)

print(f"Lista de pares: {pares}")
print(f"Lista de ímpares: {impares}")

-----------------------------------------------------------------------------
#7) Peça uma frase e conte quantas vogais há nela.
# Mostre o total de cada uma (a, e, i, o, u).

frase = input("Digite uma frase: \n")
vogais = "aeiouAEIOU" #o que está sendo pedido
contador = 0 #contador de vogais

for letra in frase:
    if letra in vogais:
        contador += 1

print(f"A frase '{frase}' contém {contador} vogais")
-------------------------------------------------------------------------------
import random

cara = 0
while(True):
    resultado = random.choice(["Cara", "Coroa"])
    print(f"Cara ou coroa??{resultado}")
    if resultado == "Cara":
        cara += 1

    else:
        cara = 0

    if cara >= 3:
        print("Cara apareceu 3 vezes seguidas!")
        break
-----------------------------------------------------------------------
#9) Crie um programa que leia uma sequência de números e
# determine quantos números são menores que a média.
num = []
size = int(input("Digite o tamanho da sequência: \n"))
for i in range(size):
    numero = int(input(f"Digite o {i+1}º número: "))
    num.append(numero)

menor = num[0]
for numero in num:
    if numero < menor:
        menor = numero

soma = sum(num)
media = soma / len(num)

print(f"O menor número é: {menor}")
print(f"A média é {media}")
-------------------------------------------------------------------------
inicio = int(input("Informe a população inicial de coelhos: "))
crescimento = float(input("Informe a porcentagem de crescimento por geração: "))
reducoes = float(input("Informe a porcentagem de mortalidade por geração: "))
ciclos = int(input("Informe o número de gerações para a simulação: "))

print("\n--- Resultados da Simulação ---\n")

for geracao in range(1, ciclos + 1):
    aumento = inicio * (crescimento / 100)
    perdas = inicio * (reducoes / 100)
    inicio += aumento - perdas
    print(f"Geração {geracao}: {int(inicio)} coelhos")

print("\n--- Fim da Simulação ---")
------------------------------------------------------------------------------------

import random

palavras = ["banana", "computador", "abacaxi", "teclado", "internet", "python"]
palavra = random.choice(palavras)

certas = []
erradas = []
tentativas = 6

print("=== Jogo da Forca ===")

while tentativas > 0:
    mostrada = ""
    for letra in palavra:
        if letra in certas:
            mostrada += letra + " "
        else:
            mostrada += "_ "

    print(f"\nPalavra: {mostrada.strip()}")
    print(f"Erradas: {' '.join(erradas)}")
    print(f"Tentativas restantes: {tentativas}")

    tentativa = input("Chuta uma letra: ").lower()

    if tentativa in certas or tentativa in erradas:
        print("Você já tentou essa letra.")
        continue

    if tentativa in palavra:
        certas.append(tentativa)
    else:
        erradas.append(tentativa)
        tentativas -= 1

    if all(letra in certas for letra in palavra):
        print(f"\nAcertou tudo! A palavra era: {palavra}")
        break
else:
    print(f"\nAcabou! A palavra era: {palavra}")
-------------------------------------------------------------------------
