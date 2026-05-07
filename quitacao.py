import utilv2


def simular_quitacao():
    utilv2.limpar_tela()
    valor_divida = float(input("Digite o valor da dívida que você quer quitar: R$"))
    float(input("Digite a sua renda mensal média: R$"))
    mes = 1
    while valor_divida > 0:
        valor_pago = float(input(f"Quanto da sua dívida você vai pagar esse mês? R$"))
        utilv2.limpar_tela()
        if valor_pago < valor_divida:
            valor_divida -= valor_pago
            valor_divida *= 1.15
            print(f"No mês {mes}, você pagou R${valor_pago:.2f}. Restam R${valor_divida:.2f} para quitar a dívida.")
            mes += 1
        if valor_pago == valor_divida:
            print(f"Parabéns! Você quitou a sua dívida!")
            break
        elif valor_pago > valor_divida:
            print(f"Parabéns! Você quitou a sua dívida e ainda tem um saldo positivo de R${valor_pago - valor_divida:.2f}!")
            break
        

if __name__ == "__main__":
    simular_quitacao()