# Organizador de Line-up do Festival
print("Bem-vindo ao sistema de organização de palco do Marco Zero!")
print("Hoje teremos uma noite de Rap e Manguebeat.")
print()

atracao_um = input("Qual o nome do primeiro MC ou banda? ") 

atracao_dois = input("Qual o nome da segunda atração? ")
atracao_tres = input("E a atração principal, quem é? ")

horario_inicio = "19:00"
horario_meio = "21:00"
horario_fim = "23:30"

print("--- CRONOGRAMA OFICIAL ---")

print(f"Às {horario_inicio}, o palco abre com {atracao_um}.")

print(f"Logo depois, às {horario_meio}, teremos o show de {atracao_dois}.")

print("Para fechar a noite:")

print("Atração Principal:", atracao_tres)

mensagem_final = input("Deixe uma mensagem para o público: ")
print("O recado da produção é:")
print(mensagem_final)
