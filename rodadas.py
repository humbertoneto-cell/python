rodada = 1
total = 0

while rodada <= 5:
    pontos = int(input(f"Quantos pontos você fez nessa rodada? "))
    total += pontos
    rodada += 1

print(f"Em cinco rodadas você fez {total} pontos.")