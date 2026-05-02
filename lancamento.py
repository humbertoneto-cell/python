import time

segundos = int(input("Quantos segundos faltam para o lançamento?"))

while segundos >= 0:
    print('\r', f"Faltam {segundos} segundos para o lançamento.", end='')
    time.sleep(1)
    segundos -= 1

print('\n', "Lançamento realizado com sucesso!")