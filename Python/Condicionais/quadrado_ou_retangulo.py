lado1 = float(input("Digite o valor do lado 1: "))
lado2 = float(input("Digite o valor do lado 2: "))
lado3 = float(input("Digite o valor do lado 3: "))
lado4 = float(input("Digite o valor do lado 4: "))

if lado1 == lado2 == lado3 == lado4:
    print("É um quadrado!")
elif (lado1 == lado3 and lado2 == lado4) or (lado1 == lado2 and lado3 == lado4):
    print("É um retângulo!")
else:
    print("Não é nem quadrado nem retângulo. O que será???")
