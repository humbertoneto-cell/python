import os
import random
import time

LARGURA = 20
ALTURA = 10

cobra = [[5, 5], [5, 4], [5, 3]]
direcao = "d"

comida = [
    random.randint(1, ALTURA - 2),
    random.randint(1, LARGURA - 2)
]


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def desenhar():
    limpar_tela()

    for linha in range(ALTURA):

        for coluna in range(LARGURA):

            if linha == 0 or linha == ALTURA - 1 or coluna == 0 or coluna == LARGURA - 1:
                print("#", end="")

            elif [linha, coluna] == comida:
                print("@", end="")

            elif [linha, coluna] in cobra:
                print("O", end="")

            else:
                print(" ", end="")

        print()

    print("\nUse:")
    print("w = cima")
    print("s = baixo")
    print("a = esquerda")
    print("d = direita")


def mover():
    global comida

    cabeca = cobra[0].copy()

    if direcao == "w":
        cabeca[0] -= 1

    elif direcao == "s":
        cabeca[0] += 1

    elif direcao == "a":
        cabeca[1] -= 1

    elif direcao == "d":
        cabeca[1] += 1

    # colisão parede
    if (
        cabeca[0] == 0
        or cabeca[0] == ALTURA - 1
        or cabeca[1] == 0
        or cabeca[1] == LARGURA - 1
    ):
        return False

    # colisão corpo
    if cabeca in cobra:
        return False

    cobra.insert(0, cabeca)

    # comeu comida
    if cabeca == comida:
        comida = [
            random.randint(1, ALTURA - 2),
            random.randint(1, LARGURA - 2)
        ]
    else:
        cobra.pop()

    return True


while True:

    desenhar()

    nova_direcao = input("Direção: ").lower()

    if nova_direcao in ["w", "a", "s", "d"]:
        direcao = nova_direcao

    vivo = mover()

    if not vivo:
        limpar_tela()
        print("GAME OVER!")
        print(f"Tamanho final da cobra: {len(cobra)}")
        break

    time.sleep(0.1)
    