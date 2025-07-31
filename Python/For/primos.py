print("Crie um programa que peça dois números inteiros, e exiba todos os números entre eles que são primos.")
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
