import random

cara = 0
while(True):
    resultado = random.choice(["Cara", "Coroa"])
    print(f"Cara ou coroa??{resultado}")
    if resultado == "Cara":
        cara += 1

    else:
        cara = 0

    if cara >= 3:
        print("Cara apareceu 3 vezes seguidas!")
        break
