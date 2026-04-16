eps = int(input("Quantos episódios essa série tem? "))
tempo = int(input("Quantos minutos cada episódio possui? "))
minutos = tempo * eps
horas = minutos/60
print()
print(f"Para terminar a série, você precisará de {minutos} minutos, ou {horas:.0f} horas.")