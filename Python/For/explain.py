# for repetição limitada

#Ex:
Lista_mercado = ["Leite", "Frutas", "Carne"]
for qualquer in Lista_mercado: #qualquer = i, pode colocar qualquer coisa aq
    print(qualquer)

for contador in range(0,6): #define o intervalo da lista
    print(contador) #conta até 5


lista = [1,2,3,4,5,6,7,8,9,10] #lista que pode ser pedida pelo usuário com um int
for num in lista: # num = i
    if num % 2 == 0: #imprimir números pares
        print(num)

for i in range (0,101,2): #ele vai imprimir maior que 1, até 100 e de 2 em 2
    print(i)

for caracter in "Computer Science": #string
    print(caracter)


#loop for aninhado
for i in range(0,5): #Faz de 0 a 5
    for a in range(0,5): #repete 5 vezes, for dentro de for
        print(a)


listas = [[1,2,3], [10,15,14], [10,1,8,7,2.3]]
for valor in listas:
    print(valor)
