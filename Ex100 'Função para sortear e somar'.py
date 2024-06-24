from random import randint

num = list()

def sorteio(lista):
    print('Sorteio dos valores da lista:')
    for intervalo in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}' , end = ' ')

sorteio(num)

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor %2 == 0:
            soma += valor
    print(f'\nA soma dos valores pares de {lista} é igual a {soma}.')

somapar(num)