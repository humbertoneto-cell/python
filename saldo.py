saldo = float(input("Qual o seu saldo atual no banco? "))
boleto = float(input("Qual o valor do próximo boleto que você deve pagar? "))
subtr = float(saldo - boleto)

print()
print(f"Tá certo. O saldo da sua conta: R${saldo:.2f} e o valor do boleto: {boleto:.2f} foram registrados.")
print(f"Agora o saldo da sua conta está em: R${subtr:.2f}.")