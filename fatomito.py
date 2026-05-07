import random


def fato_financeiro():
    numero = random.randint(1, 5)
    if numero == 1:
        print("FATO FINANCEIRO: O endividamento no Brasil bateu recorde em 2026, com 80% das famílias endividadas.")
    elif numero == 2:
        print("FATO FINANCEIRO: Em 2025, o número de inadimplentes no Brasil ultrapassou 82 milhões.")
    elif numero == 3:
        print("FATO FINANCEIRO: A inflação no Brasil atingiu 10% em 2025, a maior desde 2014.")
    elif numero == 4:
        print("FATO FINANCEIRO: O governo anunciou um plano de redução da dívida pública para 2026.")
    elif numero == 5:
        print("FATO FINANCEIRO: O mercado financeiro brasileiro apresentou alta em 2025, com aumento de 15% no Índice Bovespa.")

def  mito_financeiro():
    numeros = random.randint(1, 5)
    if numeros == 1:
        print("MITO FINANCEIRO: A poupança é o melhor investimento.")
    elif numeros == 2:
        print("MITO FINANCEIRO: O investimento em ações é sempre rentável.")
    elif numeros == 3:
        print("MITO FINANCEIRO: O dinheiro ganho com jogos de azar é seguro.")
    elif numeros == 4:
        print("MITO FINANCEIRO: O empréstimo é a solução perfeita para problemas financeiros.")
    elif numeros == 5:
        print("MITO FINANCEIRO: O investimento em imóveis é o caminho para a riqueza.")
