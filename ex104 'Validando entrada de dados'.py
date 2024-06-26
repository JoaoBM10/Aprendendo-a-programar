def leiaInt(msg):
    numero = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            numero = True
        else:
            print('ERRO! Digite um número inteiro válido.')
        if numero:
            break
    return valor

num = leiaInt('Digite um número:')
print(f'Você acabou de digitar o número {num}')