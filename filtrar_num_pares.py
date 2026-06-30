numeros = input("Digite os números separados por espaço: ").split() 
pares = filter(lambda x: int(x) % 2 == 0, numeros) 
print("Números pares:", " ".join(pares)) 

#filter = filtrar somente pares
#lambda = analisa se o filtro esta certo e deixa passar, analisa
#int(x) = o valor que nao sabemos se for dividido por 2 e o resto for 0, ele é par
#join organiza e separa por espaços
#split = tranforma numero em lista para filter filtrar a lista

numero = input("Digite um número separado por espaço: ").split()
impares = filter(lambda x: int(x) % 2 != 0, numero)
print('Numeros impares:', " ".join(impares))


produto = input("Digite o nome do produto, separado por virgula: ").split(',')
preco = (input("Digite o preço do produto, separado por virgula: ")).split(',')
#.split(',') esta colocando como que o split vai separar cada valor da lista

#zip = junta duas listas em uma so

for produto , preco in zip(produto, preco):
    print(f"Produto: {produto}, Preço: R${preco}")
