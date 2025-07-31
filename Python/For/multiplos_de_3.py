print("peça 10 números e conte quantos são multiplos de 3")
contador = 0
for num in range(10):
    int = input("Digite um número: \n")
    if num %3 == 0:
        contador += 1
        print("Multiplo de 3")
    else:
        print("Não é multiplo de 3")

print(f"A quantidade de números múltiplos de 3 é: {contador} ")
