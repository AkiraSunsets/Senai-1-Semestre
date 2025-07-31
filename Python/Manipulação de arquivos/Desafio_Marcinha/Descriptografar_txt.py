# Descriptografa mensagens usando a cifra de César com deslocamento fixo

def descriptografar(texto, deslocamento=3):
    texto_claro = ""
    for caractere in texto:
        if caractere.isalpha():
            base = ord('A') if caractere.isupper() else ord('a')
            nova = chr((ord(caractere) - base - deslocamento) % 26 + base)
            texto_claro += nova
        else:
            texto_claro += caractere
    return texto_claro

with open("texto_criptografado.txt", encoding="utf-8") as arquivo:
    conteudo = arquivo.readlines()

for linha in conteudo:
    original = descriptografar(linha.strip())
    print(original, "\n")
