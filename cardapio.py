escolha = True

while escolha:
    print()
    print("Esse é o cardápio do nosso restaurante!")
    print("Você tem 3 opções de carne")
    print("[1] Frango")
    print("[2] Carne")
    print("[3] Peixe")
    print("[4] Sair")
    print()
    carne = int(input("Qual carne você deseja? "))
    if carne == 1:
        print("Você escolheu frango.")
        escolha = False
    elif carne == 2:
        print("Você escolheu carne.")
        escolha = False
    elif carne == 3:
        print("Você escolheu peixe.")
        escolha = False
    elif carne == 4:
        escolha = False 
    else:
        print("Opção inválida. Tente novamente.")
        continue