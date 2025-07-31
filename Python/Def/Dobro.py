print("Imprimir o dobro de um número")
def dobro(num):

    calculo = num * 2
    return calculo

num = int(input("Digite um número: \n"))

resultado = dobro(num)

print(f"O dobro de {num} é {resultado}")

#--------------------------------------------

print("outra forma")
def dobro(numero):
    return numero * 2

numero = float(input("Digite um número: \n"))
print(dobro(numero))
