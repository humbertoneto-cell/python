# Simulador de Sobrevivência na UFRPE - Nível 1
print("Bem-vindo ao simulador do DC!")
print("Seu objetivo é chegar na aula de P1 sem se atrasar.")

# Capturando os dados do jogador
nome_aluno = input("Qual o seu nome? ")
curso = input("Você é de Bacharelado em Ciência da Computação ou Licenciatura em Computação? ")

print(f"Certo, {nome_aluno}, vamos começar nossa jornada saindo do RU.") 

print("A fila do almoço estava gigante, mas você conseguiu comer o frango assado.")

proximo_passo = input("Você vai de (A) Ônibus Circular ou (B) Andando pela rua de trás? ")

if proximo_passo == "A":
    print("Você escolheu ir andando pela rua de trás.") 
elif proximo_passo == "B":
    print("Você escolheu ir com o ônibus circular.")
else:
    print("ERRO!!!!!")
print("De repente, começa a chover muito forte na Várzea!")
clima_atual = "Chuva intensa"
print(f"Atenção, o clima mudou para: {clima_atual}")

print("Apesar dos desafios, você chegou ao DC. Fim da primeira etapa!")
