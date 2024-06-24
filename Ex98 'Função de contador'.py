from time import sleep

def contador(inicio, fim, passo):
    print('='*40)
    print(f'A contagem de {inicio} até {fim} de {passo} em {passo}.')
    for contagem in range(inicio, fim+1, passo):
        print(f'{contagem}', end=' ', flush = True)
        sleep(0.5)
    print()
    print('FIM')

contador(1, 10, 1)
contador(10, 0, -2)
print('='*40)
print('Escolha os valores da contagem.')
print('='*40)
i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo:'))
contador(i, f, p)