lista = list()

while True:
    valor = int(input('Digite um número:'))
    lista.append(valor)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('Valor inválido.')
print('=-'*20)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}') 
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')

