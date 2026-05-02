import time

arquivo = 1
progresso = 0

while arquivo < 4:
    while progresso < 101:
        print('\r', f"Baixando arquivo {arquivo}: {progresso}%", end='')
        time.sleep(0.1)
        progresso += 1
    print()
    arquivo += 1
    progresso = 0