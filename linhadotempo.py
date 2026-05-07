def linha_do_tempo():
    divida = float(input("Qual a sua dívida atual? R$"))
    for i in range(1, 6):
        juros = divida * 1.05
        print(f"No {i}° mês a sua dívida de R${divida:.2f} vira R${juros:.2f}.")
        divida = juros


linha_do_tempo()