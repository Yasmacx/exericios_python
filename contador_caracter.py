#ele conta o numero de palavras na frase e conta letras na palavra

def contar_palavras():
    return len(palavras)

palavras = input("Digite uma frase: ").split()
print(f'A frase que você digitou possui {contar_palavras()} palavras.')

def contar_letras():
    return len(palavra)

palavra = input("Digite uma palavra: ")
print(f'A palavra que você digitou possui {contar_letras()} letras.')
