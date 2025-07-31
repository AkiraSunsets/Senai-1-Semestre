hora = int(input("Digite a hora (0-23): "))
minuto = int(input("Digite os minutos (0-59): "))
segundo = int(input("Digite os segundos (0-59): "))

if 0 <= hora < 24 and 0 <= minuto < 60 and 0 <= segundo < 60:
    print("A hora é válida!")
else:
    print("A hora é inválida!")
