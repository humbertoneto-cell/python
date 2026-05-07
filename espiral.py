import random


def espiral_de_perdas():
    saldo = 500
    while saldo > 0:
        aposta = float(input(f"O seu saldo é de R${saldo:.2f}. Você vai apostar R$"))
        if aposta > saldo:
            print("Você não pode apostar esse valor.")
            continue
        saldo -= aposta
        numero = random.randint(1, 10)
        if numero in [9,10]:
            print("Parabéns! A sua aposta foi creditada!")
            saldo += aposta * 2
        else:
            print("Infelizmente, você perdeu a aposta.")
        print(f"O seu saldo atual é de R${saldo:.2f}")
    print("Você perdeu todo o seu saldo! A espiral de perdas é real!")

espiral_de_perdas()