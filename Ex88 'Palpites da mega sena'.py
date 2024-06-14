from random import randint

print('='*40)
print(f'{'JOGA NA MEGA SENA':^40}')
print('='*40)

lista = []
totaljogos = 1
jogos = []

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))

while totaljogos <= quantidade:
    contador = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totaljogos += 1
print(f'{f'< SORTEANDO {quantidade} JOGOS >':=^40}')

for indice, lista in enumerate(jogos):
    print(f'Jogo {indice+1}:{lista}')
print(f'{'< BOA SORTE >':=^40}')