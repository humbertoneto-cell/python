senha_correta = "tapioca"
senha = input("Tente advinhar a senha: ")

while senha != senha_correta:
    senha = input("Tente advinhar a senha: ")
    if senha == "tapioca":
        print("Parabéns, você acertou a senha!")
        break
    elif senha == "desisto":
        print("Fim de jogo!")
        break

