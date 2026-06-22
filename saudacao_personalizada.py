def saudacoes_personalizada():
    nome = input("Digite seu nome: ")

    horario = int(input("Digite a hora atual (0-23): "))
    if 0 <= horario < 12:
        saudacao = 'Bom dia!'
    elif 12 <= horario < 18:
        saudacao = 'Boa tarde!'
    elif 18 <= horario < 24:
        saudacao = 'Boa noite!'
    
    print(f"Olá, {nome}, {saudacao}")

saudacoes_personalizada()
