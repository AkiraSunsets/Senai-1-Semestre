print(" Peça 10 números e separe em duas listas: pares e ímpares. Mostre as duas no final. Inicializando as listas de pares e ímpares")
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
