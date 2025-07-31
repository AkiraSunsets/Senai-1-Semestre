print("Jogo de Adivinhação - Você tem 2 chances para acertar o número!")
numero = random.randint(1, 10)

chance1 = int(input("Insira um número (1 a 10): "))
resultado = ""

if chance1 == numero:
    resultado = "Parabéns! Você acertou de primeira!"
else:
    if chance1 > numero:
        print("O número é menor!")
    else:
        print("O número é maior!")

    chance2 = int(input("Sua última tentativa. Insira o número: "))
    if chance2 == numero:
        resultado = "Parabéns! Você acertou!"
    elif chance2 > numero:
        resultado = "Você errou! O número era menor!"
    else:
        resultado = "Você errou! O número era maior!"

print(f"{resultado}\nO número era: {numero}")
