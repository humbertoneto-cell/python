divida_inicio = 2000
mes = 1

while mes <= 12:
    print(f"Com os juros, a dívida atual é de: R${divida_inicio:.2f}")
    pagamento = float(input("Quanto você vai pagar esse mês? "))
    if pagamento < (divida_inicio/10):
        print("Pagamento inválido. Informe um valor maior.")
        continue
    elif divida_inicio <= 0:
        print()
        print("Parabéns, você quitou a dívida!")
        break
    else:
        divida_inicio -= pagamento
        divida_inicio *= 1.15
mes += 1

