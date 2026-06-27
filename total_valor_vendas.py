print('==========================')
print('Bem-vindo ao sistema de vendas!')
print('==========================')

def calcular_vendas():
    vendas = map(int, input("Digite os valores das vendas separados por espaço: ").split())
    total = sum(vendas)
    print(f"O total de vendas é: R${total}")

#map é converter input em numero
#sum soma todos os valores 
calcular_vendas()

#int > um valor
#map(int,input ( ))> varios valores
