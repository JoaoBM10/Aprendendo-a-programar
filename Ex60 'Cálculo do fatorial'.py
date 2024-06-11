num = int(input('Digite um número para calcular seu fatorial:'))
cont = num
fatorial = 1 
print(f' Calculando {num}! = ', end = '')
while cont > 0:
    print(f'{cont}', end = '')
    print(' x ' if cont > 1 else ' = ', end = '')
    fatorial *= cont
    cont -= 1
print(f'{fatorial}')