idade1 = int(input("Digite sua idade:"))
idade2 = int(input("Digite outra idade:"))
idade3 = int(input("Digite outra idade:"))

maior = idade1
if idade2 > idade1 and idade2 > idade3:
    maior = idade2

if idade3 > idade1 and idade3 >= idade2:
    maior = idade3

menor = idade1
if idade2 < idade3 and idade2 < idade1:
    menor = idade2

if idade3 <= idade2 and idade3 < idade1:
    menor = idade3

print(f"A menor idade é: {menor}")
print(f"A maior idade é: {maior}")
