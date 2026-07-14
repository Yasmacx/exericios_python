def soma_recustiva(n):
    if n == 1:
        return 1
    return n + soma_recustiva(n - 1)

numero = int(input("Digite um número para calcular a soma recursiva: "))
resultado = soma_recustiva(numero)
print(resultado)

#() parametro é ate quantas vezes vai somar
#n == 1 é onde o computador vai sumir ate ser igual esse parametro
#return vai devolver resultado
#n = numero inicial do parametro
#n (5) = 5 + 4 + 3 + 2 + 1 

def multi_recustiva(n):
    if n == 1:
        return 1
    return n * multi_recustiva(n - 1)

numero = int(input("Digite um número para calcular a multiplicação recursiva: "))
resultado = multi_recustiva(numero)
print(resultado)
