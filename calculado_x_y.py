soma = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y if y != 0 else "Erro: Divisão por zero"

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == '+':
    resultado = soma(x, y)
elif operacao == '-':
    resultado = subtracao(x, y)
elif operacao == '*':
    resultado = multiplicacao(x, y)
elif operacao == '/':
    resultado = divisao(x, y)
else:
    resultado = "Operação inválida"

print(f"O resultado é: {resultado}")
