from random import randint
from time import sleep
from operator import itemgetter

jogadas = {"Player1": randint(1,6), 
           "Player2": randint(1,6),
           "Player3": randint(1,6),
           "Player4": randint(1,6)}

ranking = list()

print('Valores sorteados:')
for keys, values in jogadas.items():
    print(f'{keys} tirou {values} no dado.')
    sleep(2)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('='*30)
print(' == RANKING DOS JOGADORES == ')
for indice, valor in enumerate(ranking):
    print(f' {indice+1}° lugar: {valor[0]} com {valor[1]}.')
    sleep(1)