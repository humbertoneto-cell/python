salario = float(input("Qual é o salário do seu estágio? "))
inicio = float(input("Quanto você pretende investir por mês? "))
continua = True
investimento = inicio * 1.01

while continua:
        print(f"O seu investimento está em R${investimento:.2f}")
        extra = input("Deseja continuar investindo? (s/n) ")
        if extra.lower() == "n":
            continua = False
        if extra.lower() == "s" or "":
            continue

        investimento += inicio 
        investimento *= 1.01
