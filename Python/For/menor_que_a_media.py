print("Crie um programa que leia uma sequência de números e determine quantos números são menores que a média.")
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
