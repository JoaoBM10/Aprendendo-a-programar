listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)

for posicao in range(0, len(listagem),2):
    print(f'{listagem[posicao]:.<30}', end='')
    print(f'R${listagem[posicao+1]:>7.2f}')
print('-'*40)

#Outro método

print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)

for posicao in range(0, len(listagem)):
    if posicao %2 == 0:
        print(f'{listagem[posicao]:.<30}', end='')
    else:
        print(f'R${listagem[posicao]:>7.2f}')
print('-'*40)