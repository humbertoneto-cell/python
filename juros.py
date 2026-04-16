#10 a 15% ao mês
#Máximo de 8% ao mês
#Até 1,9% ao mês

salario = float(input("Qual é o seu salário atual? "))
contas = float(input("Qual o valor total das suas contas fixas? "))
cheque = float(input("De quanto é a sua dívida no cheque especial? "))
resto = salario - contas - cheque

print()
print(f"Considerando que todas as suas dívidas sejam pagas hoje, sobra R${resto:.2f}.")