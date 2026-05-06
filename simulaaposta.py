investido = float(input("Digite um valor que você vai investir em apostas: R$"))


def simular_aposta(investido):
    print()
    margem = investido * 0.15
    resto = investido - margem
    print(f"Você apostou R${investido:.2f}, a casa ficou com R${margem:.2f}. Você sacou R${resto:.2f}.\nLembre-se, a casa sempre vence!")

simular_aposta(investido)
