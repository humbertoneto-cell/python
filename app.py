import utilv2

def main():
    utilv2.limpar_tela()
    utilv2.cabecalho_bonito()
    print("Bem-vindo ao bcc bank!")
    nome = input("Qual o seu nome? ")
    utilv2.limpar_tela()
    utilv2.cabecalho_bonito()
    print(f"Olá, {nome}! Vamos organizar as finanças.")


if __name__ == "__main__":
    main()