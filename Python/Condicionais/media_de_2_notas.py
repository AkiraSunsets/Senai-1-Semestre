nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

menor_nota = min(nota1, nota2, nota3)

media = (nota1 + nota2 + nota3 - menor_nota) / 2

print(f"A média das duas maiores notas é: {media:.2f}")
