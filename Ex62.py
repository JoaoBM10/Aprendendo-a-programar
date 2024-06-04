print('Gerador de PA')
print('=-='*8)

#variaveis para primeiro while
total_termos = 0
inicio = 10

#variaveis para segundo while
primeiro_termo = int(input('Primeiro termo:'))
razao = int(input('Razão da PA:'))
contador = 1

while inicio != 0:
    total_termos += inicio 
    while contador <= total_termos:
        print(f'{primeiro_termo} -> ', end = '')
        primeiro_termo += razao
        contador += 1 
    print('Pausa')
    inicio = int(input('Quantos termos você quer mostrar a mais?'))
print('FIM')