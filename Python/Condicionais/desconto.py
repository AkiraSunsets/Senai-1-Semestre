produto = int(input("Digite a quantidade de produtos a ser adquirido: "))
valor = float(input("Digite o preço de cada unidade: "))

if produto > 100:
    print("Você ganhou desconto de 10%")

elif produto < 100:
    print("Você ganhou desconto de 5%")

print(valor)

if produto > 100:
    condicao1= valor * 0.9
    print(f"Você pagará o total de {condicao1} ao final de sua compra")

elif produto < 100:
    condicao2 = valor * 0.5
    print(f"Você pagará o total de {condicao2} ao final de sua compra")
