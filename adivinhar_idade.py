#calculo que faz conta pelo ano que nasceu menos ano atual para descobrir idade

def calcular_idade():

    atual = int(input("Digite o ano atual: "))
    idade = int(input("Digite o ano de nascimento: "))
    calcular = atual - idade
    print(f"Sua idade é: {calcular} anos!")

calcular_idade()
