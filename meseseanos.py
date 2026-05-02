mes = 1
ano = 1
poupanca = 0

while ano < 4:
    while mes < 13:
        poupanca += 100
        mes += 1
    print(f"Fim do ano {ano}. Saldo acumulado de: R${poupanca:.2f}")
    mes = 1
    ano += 1