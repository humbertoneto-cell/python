valor = float(input("Em quanto está a sua dívida hoje? "))
tempo = int(input("Por quantos meses você pretende continuar com essa dívida? "))
final = valor * (1.15 ** tempo)

print()
print(f"O valor final da sua dívida ficará em {final:.2f}")