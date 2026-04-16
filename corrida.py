quilometro = float(input("Quantos quilômetros você correu na sua últoma corrida? "))
tempo = int(input("Em quanto tempo[minutos] você finalizou a corrida? "))
pace = (tempo/quilometro)

print()
print(f"Você correu {quilometro} quilômetros em {tempo} minutos num pace de {pace:.2f}.")