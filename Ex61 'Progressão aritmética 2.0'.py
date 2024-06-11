print('Gerador de PA')
print('=-='*8)

primeiro_termo = int(input('Primeiro termo:'))
razao = int(input('Razão da PA:'))
contador = 1

while contador <= 10:
    print(f'{primeiro_termo} -> ', end = '')
    primeiro_termo += razao
    contador += 1    
print('FIM')
