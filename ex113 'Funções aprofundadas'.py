def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mNúmero inteiro inválido, tente novamente.\033[m')
        else:
            return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mNúmero real inválido, tente novamente:\033[m')
        else:
            return num


numero = leiaint('Digite um número inteiro:')
numero2 = leiafloat('Digite um número real:')
print(f'Você digitou o número inteiro {numero}.')
print(f'Você digitou o número real {numero2}.')