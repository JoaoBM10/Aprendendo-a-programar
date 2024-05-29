from time import sleep
import random

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada?'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)

itens = ('Pedra','Papel','Tesoura')
pc = random.randint(0,2)
print('Computador jogou {}'.format(itens[pc]))
if jogador == 0:
    print('Jogador jogou Pedra')
elif jogador == 1:
    print('Jogador jogou Papel')
else:
    print('Jogador jogou Tesoura')

print('-=' * 11)

if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    else:
        print('COMPUTADOR VENCEU')
elif pc == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    else:
        print('JOGADOR VENCEU')
else:
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    else:
        print('EMPATE')



