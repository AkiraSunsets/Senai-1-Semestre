inicio = int(input("Informe a população inicial de coelhos: "))
crescimento = float(input("Informe a porcentagem de crescimento por geração: "))
reducoes = float(input("Informe a porcentagem de mortalidade por geração: "))
ciclos = int(input("Informe o número de gerações para a simulação: "))

print("\n--- Resultados da Simulação ---\n")

for geracao in range(1, ciclos + 1):
    aumento = inicio * (crescimento / 100)
    perdas = inicio * (reducoes / 100)
    inicio += aumento - perdas
    print(f"Geração {geracao}: {int(inicio)} coelhos")

print("\n--- Fim da Simulação ---")
