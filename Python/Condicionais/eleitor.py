idade = int(input("Insira sua idade: "))
if idade < 18:
    print("Não eleitor")

elif 18 <= idade <= 69:
    print("Voto obrigatório")

else:
    print("Voto facultativo")
