lista = []
listapar = []
listaimpar = []

while True:
    valor = int(input('Digite um número:'))
    lista.append(valor)
    if valor %2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('Valor inválido.')
print(f'A lista completa é {lista}.')
print(f'A lista de pares é {listapar}.')
print(f'A lista de impares é {listaimpar}.')

#Se já tiver a lista pronta e querer jogar os valores em outra lista, pode fazer assim:

for pos , valor in enumerate(lista):
    if valor %2 == 0:
        listapar.append(valor)
    elif valor %2 == 1:
        listaimpar.append(valor)