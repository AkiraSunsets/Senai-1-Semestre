Funções

É um bloco de código autônomo e reutilizavel que é designado para realizar uma tarefa especifica 

```python
def nome_da_funcao(parametro1,parametro2,...)
# Corpo da função
```

Exemplo:

```python
def saudacao():
    print("Hello World")

saudacao()
```

Exercicio exemplo:

```python
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
```

É a variavel criada dentro de uma função

- Só existe dentro da função
- Morre(deixa de existir) quando a função termina

Exemplo:

```python
def minha_funcao():
    x = 10 #variavel local
    print(x)
    minha_funcao()
print(x) #Se tentar aqui, dá erro! Porque "x" só existe dentro da função
```

- É a variavel criada fora de qualquer função
- Existe em todo o programa
- Pode ser usada dentro das funções, mas não pode ser alterada dentro delas sem um comando especial

Exemplo:

```python
y = 20

def outra_funcao():
    print(y) #pode acessar o valor global

outra_funcao()
print(y) #também pode usar aqui
```

Ah, então tenho que criar a variavel global antes de criar a função?

> → Não, inclusive clean code direciona que a função deve ser definida antes do restante do código
> 

Agora, se quiser alterar a variavel global dentro da função, precisa usar a palavra global:

Exemplo 

```python
def mudar_valor():
    global z
    z = 100
z = 5
mudar_valor()
print(z) #Agora z vale 100
```

Se não usar global, o Python entende que você está criando outra variavel com o mesmo nome, mas que é local. Olha:

```python
def tentar_mudar():
    a = 50 #isso é uma variavel local! Não muda a global
    print(a) #imprime 50

a = 7 
tentar_mudar()
print(a) #ainda imprime 7
```
