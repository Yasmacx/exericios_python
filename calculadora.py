print("====================================")
print("Calculador de Numeros Impares!")
print("====================================")

def lista_numeros():
    try:
        somar = 0
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for numero in numeros:
            print(numero)
            if numero % 2 != 0:
                somar += numero
            print(f"A soma dos números ímpares é: {somar}")
    except:
        print("Ocorreu um erro ao calcular a soma dos números ímpares.")


lista_numeros()

print("====================================")
print("Calculador de Numeros Pares!")
print("====================================")

def lista_numeros_pares():
    somar = 0
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for numero in numeros:
        print(numero)
        if numero % 2 == 0:
            somar += numero
    print(f"A soma dos números pares é: {somar}")

lista_numeros_pares()

print("====================================")
print("Calculador de todos os Números!")
print("====================================")

def lista_todos_numeros():
    somar = 0
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for numero in numeros:
        print(numero)
        somar += numero
        resultado = somar
        print(f'A soma de todos os numeros é: {resultado}')

lista_todos_numeros()
