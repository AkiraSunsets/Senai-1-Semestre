EXERCÍCIOS


#1. Calcule a soma de 2 números.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print(num1 + num2)


#2. Verifique se o número é ímpar
num = int(input("digite um número: "))
condicao = num % 2 !=0
print(f"O número {num} é impar?{condicao}")

#3. Verifique se pelo menos uma das condições é verdadeira, se valor1 é maior que 3 ou se valor 2 é menor que 4.
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
condicao = num1 > 3 or num2 < 4
print(f"Valor1 {num1} é maior que 3 ou Valor2 {num2} é menor que 4{condicao}")


#4. Calcule o valor absoluto.
num = int(input("Digite um número: "))
valor_absoluto = abs(num)
print(f"O valor absoluto de {num} é {valor_absoluto}")


#5. Verifique se ambos os valores são pares.
num = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o primeiro número: "))
print("Ambos são pares" * ((num % 2 == 0) and (num2 % 2 == 0)) or "Um dos números inseridos, não é par")


#6. Verifique se pelo menos um dos valores é negativo
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
print("Um dos valores é negativo" * ((num1 < 0) or (num2 < 0)) or "Nenhum valor é negativo")


#7. Calcule a média de 3 valores.
num1 = int(input("Insira o primeiro numero"))
num2 = int(input("Insira o segundo numero"))
num3 = int(input("Insira o terceiro numero"))
num4 = num1 + num2 + num3 / 3
print(f"A media de {num1} + {num2} + {num3} / 3 é igual a {num4}")



#8. Imprima se o resultado da expressão abaixo é True ou False:
valor1 + 15 é igual a valor2 * 3
valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))
condicao = (valor1 + 15) == (valor2 * 3)
print(f"Os valores são iguais: {condicao}" * condicao or f"Os valores são diferentes: {condicao}")


#9. Calcule o resultado e o resto da divisão entre o dividendo e o divisor. Exiba todas as informações.
num1 = int(input("Digite o valor dividendo: "))
num2 = int(input("Digite o valor divisor: "))
condicao = num1 // num2 resto = num1 % num2
print(f"Dividendo: {num1}")
print(f"Divisor: {num2}")
print(f"Resultado da divisão: {condicao}")
print(f"Resto da divisão: {resto}")


10. Escreva um programa que converta uma temperatura digitada de graus Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura:"))
f = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é {f}°F")


#11. Escreva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. O usuário deve informar seu peso em kg e altura em metros. A resposta deve ter no máximo 2 dígitos decimais.
peso = float(input("Insira seu peso em kg: "))
altura = float(input("Insira sua altura em metros: "))
imc = peso / ( altura ** 2) print(f"O seu IMC é: {imc:.2f}")


#12. Crie um programa que calcule a média ponderada de três notas, sendo que as notas têm pesos diferentes.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
peso1 = float(input("Digite o peso da primeira nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))
peso3 = float(input("Digite o peso da terceira nota: "))
media_ponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)
print(f"A média ponderada é: {media_ponderada:.2f}")


#13. Escreva um programa que calcule a potência de um número inteiro elevado a um expoente.
num1 = int(input("Digite a base, (coloque um número inteiro): "))
num2 = int(input("Digite o expoente(coloque um número inteiro): "))
potencia = num1 ** num2 print(f"o resultado de {num1} elevado a {num2} é: {potencia}")


#DESAFIO (Obrigatório):
#1. Calcule a raiz cúbica de um número.
num = float(input("Digite um valor: "))
raiz_cubica = num ** (1/3)
print(f"A raíz cúbica de {num} é {raiz_cubica:.2f}")



#2. Crie um programa que calcule o montante final após um período de tempo com juros compostos. O usuário deve informar o capital, taxa de juros e tempo em anos.
capital = float(input("Digite o capital inicial (P): "))
taxa_juros = float(input("Digite a taxa de juros anual (%): "))
tempo = int(input("Digite o tempo em anos (t): "))
montante = capital * (1 + (taxa_juros / 100)) ** tempo
print(f"O montante final após {tempo} anos é: {montante:.2f}")