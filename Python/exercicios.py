for numero in range(0, 11, 2):
#for numero in range(1,11)
#for numero in range(0,11,2)
#for numero in range(0,11,3)
    print(numero)

cores = ['azul','verde', 'amarelo']
for cor in cores:
    print(cor)

soma = 0
for i in range(1, 101):
    soma += i
    print("Soma:", soma)


tabuada = int(input("Digite um número: "))
for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))


tabuada = int(input("Digite um número: "))
for i in range(1,11):
    print(tabuada, "x", i, "=", tabuada * i)


