#estudo de como criar painel de controle, listas e dicionario

def titulo_numeros():
    print("====================================")
    print("      Bem-vindo a lista de numeros     ")
    print("====================================")

def lista_numeros():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for numero in numeros:
        print(numero)
    voltar_painel()

def titulo_nomes():
    print("====================================")
    print("      Bem-vindo a lista de nomes     ")
    print("====================================")

def lista_nomes():
    nomes = ["Yasmin", "Maria", "João", "Pedro", "Ana"]
    for nome in nomes:
        print(nome)
    voltar_painel()

def titulo_anos():
    print("====================================")
    print("      Bem-vindo a lista do ano que você nasceu e ano atual   ")
    print("====================================")

def lista_anos():
    anos = [2007, 2026]
    for ano in anos:
        print(ano)
    voltar_painel()

def titulo_painel():
    print("====================================")
    print("      Bem-vindo ao painel de informações     ")
    print("====================================")

def sair():
    print("\n" * 100)
    print("Saindo do programa...")
    exit()

def voltar_painel():
    escolha = input("Deseja voltar ao painel de informações? (s/n): ")
    if escolha.lower() == 's':
        print("\n" * 100)
        painel_informacoes()

def painel_informacoes():
    titulo_painel()
    print('Escolha uma das opções abaixo:')
    print('1 - Lista de números')
    print('2 - Lista de nomes')
    print('3 - Lista de anos')
    print('4 - Sair')
    
    escolha = input('Digite o número da opção desejada: ')
    if escolha == '1':
        titulo_numeros()
        lista_numeros()
    elif escolha == '2':
        titulo_nomes()
        lista_nomes()
    elif escolha == '3':
        titulo_anos()
        lista_anos()
    elif escolha == '4':
        sair()
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')


def main():
    painel_informacoes()   

if __name__ == '__main__':
    main()
