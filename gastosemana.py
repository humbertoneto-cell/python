gasto_total = 0
gasto = True

while gasto:
    gasto = float(input("Quanto você gastou essa semana? "))
    gasto_total += gasto
    if gasto <= 0:
        gasto = False

print(f"Nas últimas semanas você gastou R${gasto_total:.2f}") 