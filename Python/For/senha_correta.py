print("senhas infinitas até encontrar a certa")
senha_correta = "1234"

while True: #loop infinito até encontrar a senha correta.
    senha = input("Digite a senha: \n")

    if senha == senha_correta:
        print("Senha correta!")
        break  # encerra o loop quando a senha estiver correta.
    else:
        print("Senha incorreta, tente novamente.")
