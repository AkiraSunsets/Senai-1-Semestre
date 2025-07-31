print("Peça uma frase e conte quantas vogais há nela. Mostre o total de cada uma (a, e, i, o, u).")
frase = input("Digite uma frase: \n")
vogais = "aeiouAEIOU" #o que está sendo pedido
contador = 0 #contador de vogais

for letra in frase:
    if letra in vogais:
        contador += 1

print(f"A frase '{frase}' contém {contador} vogais")
