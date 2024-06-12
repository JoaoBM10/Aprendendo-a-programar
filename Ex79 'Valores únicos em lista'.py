valores = list()

while True:
    valor = input('Digite um valor:')
    try:
        valor = int(valor)
        if valor not in valores:
            valores.append(valor)
            print('Valor adicionado com sucesso...')
        else:
            print('Valor duplicado não é aceitável.')
    except ValueError:    
        print('Por favor, digite um valor inteiro válido.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('Valor inválido.')
print('='*40)
valores.sort()
print(f'Você digitou os valores {valores}.')
