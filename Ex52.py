num = int(input('Digite um número:'))
cont = 0
for intervalo in range(1 , num + 1 , 1):
    if num % intervalo == 0:
        cont += 1
        print('\033[33m', end = ' ')
    else:
        print('\033[31m', end = ' ')
    print(f'{intervalo}', end = ' ')
print(f'\n\033[m O número escolhido foi dividido {cont} vezes')
if cont == 2:
    print('O número escolhido é primo!')
else:
    print('O número escolhido não é primo!')