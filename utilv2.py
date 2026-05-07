import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def cabecalho_bonito():
    print("=" * 50)
    print(" " * 21 + "BCC BANK" + " " * 21)
    print("=" * 50)


if __name__ == "__main__":
    limpar_tela()