import random

palavras = ["banana", "computador", "abacaxi", "teclado", "internet", "python"]
palavra = random.choice(palavras)

certas = []
erradas = []
tentativas = 6

print("=== Jogo da Forca ===")

while tentativas > 0:
    mostrada = ""
    for letra in palavra:
        if letra in certas:
            mostrada += letra + " "
        else:
            mostrada += "_ "

    print(f"\nPalavra: {mostrada.strip()}")
    print(f"Erradas: {' '.join(erradas)}")
    print(f"Tentativas restantes: {tentativas}")

    tentativa = input("Chuta uma letra: ").lower()

    if tentativa in certas or tentativa in erradas:
        print("Você já tentou essa letra.")
        continue

    if tentativa in palavra:
        certas.append(tentativa)
    else:
        erradas.append(tentativa)
        tentativas -= 1

    if all(letra in certas for letra in palavra):
        print(f"\nAcertou tudo! A palavra era: {palavra}")
        break
else:
    print(f"\nAcabou! A palavra era: {palavra}")
