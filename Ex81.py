lista = []
posicao = 0
for x in range(0,5):
    valor = int(input('Digite um valor: '))
    for n in lista:
        if n < valor :
            posicao +=1  
    lista.insert(posicao, valor)
    posicao = 0
    if x == 0:
        print('Adicionado ao final da lista...')
    else:
            if len(lista) == lista.index(valor)+1:
                 print(f'Adicionado ao final da lista...')
            else:
              print(f'Adicionado a posição {lista.index(valor)} da lista...')
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')