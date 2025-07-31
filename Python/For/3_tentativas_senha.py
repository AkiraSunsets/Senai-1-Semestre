print("O usuário tem 3 tentativas para acertar a senha. Se errar todas, o acesso é bloqueado. Use while.")
senha = 1234
contador = 0

while contador < 3:
    senha_correta = int(input("Insira sua senha: "))
    if senha == senha_correta:
        print("Welcome!")
        break
    else:
        contador += 1
        if contador == 3:
            print("Acesso restrito")
            break
