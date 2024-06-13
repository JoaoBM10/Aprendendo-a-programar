principal = []
temporaria = []

contador_maior = contador_menor = 0

while True:
    temporaria.append(str(input('Digite o nome:')))
    temporaria.append(int(input('Digite o peso:')))
    if len(principal) == 0:
        contador_maior = contador_menor = temporaria[1]
    else:
        if temporaria[1] > contador_maior:
            contador_maior = temporaria[1]
        if temporaria[1] < contador_menor:
            contador_menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('Valor inválido.')
print('='*20)
print(f'Ao todo você cadastrou {len(principal)} pessoas.')
print(principal)
print(f'O maior peso foi de {contador_maior}Kg. Peso de ', end='')
for peso in principal:
    if peso[1] == contador_maior:
        print(f'{[peso[0]]}',end='')
print()
print(f'O menor peso foi de {contador_menor}Kg. Peso de ', end='')
for peso in principal:
    if peso[1] == contador_menor:
        print(f'{[peso[0]]}', end='')