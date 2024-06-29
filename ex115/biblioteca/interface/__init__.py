def linha(tamanho = 40):
    return '-' * tamanho


def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opcao = leiaInt('\033[32mSua opção:\033[m')
    return opcao


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Número inteiro invalido, tente novamente.')
        else:
            return n

