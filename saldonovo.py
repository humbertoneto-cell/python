renda = float(input("Qual é a sua renda total? "))
fixa = float(input("Quais são as suas despesas fixas totais? "))
varmax = float(input("Quais foi o máximo que você gastou com suas despesas variáveis? "))
varmin = float(input("Quais foi o mínimo que você gastou com suas despesas variáveis? "))
saldo = renda - ((varmax + varmin)/2 + fixa)
saldomin = renda - varmax + fixa
saldomax = renda - varmin + fixa

if saldomin >= 0:
    print(f"Cenário seguro! Mesmo no caso de maiores gastos variáveis você está no azul em R${saldomin:>2f}")

elif saldomax >= 0:
    print(f"Cenário de alerta! No caso de maiores gastos variáveis você poderá se endividar, caso garanta reduzir os gastos variáveis ao mínimo seu saldo será R${saldomax:.2f}")

else:
    print(f"Atenção: Você fechou no vermelho e seu endividamento pode variar dentre R$ {saldomin:.2f} e R$ {saldomin:.2f}. O primeiro passo é ter clareza, respire fundo. Vamos buscar soluções.")