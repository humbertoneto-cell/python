pontos_vida = 5000

while pontos_vida > 0:
    ataque = input("Você vai dar um ataque rápido ou um ataque mágico? (r/m) ")
    if ataque.lower() == "r":
        pontos_vida -= 200
    elif ataque.lower() == "m":
        pontos_vida -= 400
    else:
        print("Opção inválida. Tente novamente.")
        continue
    print(f"Pontos de vida restantes: {pontos_vida}")
print("Parabéns! Você derrotou o inimigo!")