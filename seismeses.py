mes = 1
guardou = 0

while mes <= 6:
    guardado = float(input(f"Quanto você guardou esse mês? "))
    guardou += guardado
    mes += 1

print(f"Em seis meses você guardou R${guardou:.2f}")