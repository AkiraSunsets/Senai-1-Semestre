print("Consulte seu IMC")
peso = float(input("Insira seu peso em kg: "))
altura = float(input("Insira sua altura em metros: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Baixo Peso")

elif imc >= 18.5 and imc <= 24.9:
    print("Normal")

elif imc >= 25 and imc <= 29.9:
    print("Sobre peso")

elif imc >= 30 and imc <= 34.9:
    print("Obesidade")

elif imc >= 35 and imc <= 39.9:
    print("Obesidade Mórbida")

elif imc > 40:
    print("Obesidade Mórbida")

else:
    print("Seu peso está abaixo do esperado")
