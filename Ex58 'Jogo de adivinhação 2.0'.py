from random import randint
computador = randint(0,10)

print('''Sou seu computador...
Acabei de Pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

acertou = False
tentativas = 0
while not acertou:
    palpite = int(input('Qual é seu palpite?'))
    if palpite == computador:
        acertou = True
    else:
        if palpite > computador:
            print('Menos... Tente outra vez.')
        else:
            print('Mais... Tente outra vez.')
    tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabéns')    
