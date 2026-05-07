def diagnostico_autonomo():
    custo_de_vida = float(input("Qual o seu custo de vida mensal? R$"))
    sobrevivencia = custo_de_vida * 6
    paz = custo_de_vida * 12
    print(f"A sua meta de sobrevivência é  de R${sobrevivencia:.2f}")
    print(f"A sua meta de paz de espírito é de R${paz:.2f}")

if __name__ == "__main__":
    diagnostico_autonomo()