print("media de uma lista de números")
def media_ponderada(lista):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma/len(numeros) #len significa somar os números da lista

numeros = [10,20,30]
print(media_ponderada(numeros))
