import autonomo
import utilv2
import bets
import quitacao

def main():
    menu = True
    utilv2.limpar_tela()
    utilv2.cabecalho_bonito()
    print("Bem-vindo ao bcc bank!")
    nome = input("Qual o seu nome? ")
    utilv2.limpar_tela()
    utilv2.cabecalho_bonito()
    print(f"Olá, {nome}! Vamos organizar as finanças.")
    while menu:
        print("Você tem 3 opções:")
        print("[1] - Diagnóstico de autonomia financeira")
        print("[2] - Simulador de quitação de dívidas")
        print("[3] - Alerta de apostas")
        print("[4] - Sair")
        escolha = input("Digite a opção desejada: ")
        if escolha == "1":
            menu_autonomo()
        elif escolha == "2":
            menu_quitacao()
        elif escolha == "3":
            menu_alerta_bets()
        elif escolha == "4":
            print("Obrigado por usar o bcc bank! Até a próxima!")
            menu = False
        else:
            print("Opção inválida. Por favor, tente novamente.")


def menu_autonomo():
    autonomo.diagnostico_autonomo()



def menu_alerta_bets():
    bets.alertabets()


def menu_quitacao():
    quitacao.simular_quitacao()


if __name__ == "__main__":
    main()