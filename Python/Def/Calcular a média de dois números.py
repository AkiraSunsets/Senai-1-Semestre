print("Calcular a media de 2 números")
def calcular_media(nota1,nota2):

    media = (nota1 + nota2)/2
    return media  #vai ser utilizado embaixo

#pedindo as notas do usuário
nota1 = int(input("Digite a sua primeira nota: \n"))
nota2 = int(input("Digite a sua segunda nota: \n"))

#chamando a função para calcular a media e armazenando o resultado
resultado = calcular_media(nota1,nota2)

#exibindo a média
print(f"A média entre as notas {nota1} e {nota2} é {resultado}")
