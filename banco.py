saldo = 0
operacoes = True

while operacoes:
    print()
    print("Você tem 4 opções possíveis:")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Saldo")
    print("[4] Sair")
    print()
    escolha = input("Qual operação você deseja fazer? ")
    print()
    if escolha == "1":
        deposito = float(input("Quanto deseja depositar? "))
        print()
        saldo += deposito
    elif escolha == "2" and saldo > 0:
        saque = float(input("Quanto deseja sacar? "))
        print()
        if saldo > saque:
            saldo -= saque
        else:            
            print("Saldo insuficiente para saque.")
            print()
            continue
    elif escolha == "2"and saldo <= 0:
        print("Saldo insuficiente para saque.")
        print()
        continue
    elif escolha == "3":
        print(f"Seu saldo atual é de R${saldo:.2f}")
        print()
    elif escolha == "4":
        operacoes = False
    else:        
        print("Opção inválida. Tente novamente.")
        print()
        continue

print("Obrigado por usar nosso banco. Tenha um ótimo dia!")