#1 -  Lista
frutas = ['maçã','banana','laranja']
for fruta in frutas:
    print(fruta)
print(frutas[2])

#2 - String
mensagem = 'Hello World!'
for caractere in mensagem:
    print(caractere)

#3 - Tuplas
cores = ("vermelho", "verde", "azul", "amarelo")
for cor in cores:
    print("cor:", cor)

#4 - Dicionário
pessoa ={
    "nome": "Ana",
    "idade": "30",
    "Profissão": "engenheira"
}

print(pessoa["nome"])
for chave, valor in pessoa.items():
    print(f"{chave}:{valor}")

#5 - Dicionário do Dicionário
alunos={
    "123":{
        "nome": "Lucas",
        "idade": 17
},
"456":{
    "nome": "Maria",
    "idade": 18}
}

for ra, dados in alunos.items():
    print(f"RA:{ra}")
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}") #capitalize, deixa a primeira letra maior

print(alunos["456"]["nome"]) #Acessar aluno especifico

#6 - Conjuntos
animais = {"gato", "cachorro", "elefante", "girafa"}
for animal in animais:
    print("Animal:", animal)

#7 - Range
for numero in range(5):
#for numero in range(1,11)
#for numero in range(0,11,2)
#for numero in range(0,11,3)
    print(numero)

#8 - Abrir arquivo
nome_arquivo = "C:/Users/51931882819/Documents/AKIRA.txt"
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())#strip() remove espaços em branco
