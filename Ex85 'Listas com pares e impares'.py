valor_geral = [[],[]]
contador = 0

for contador in range(0,7,1):
    contador+=1
    valor = int(input(f'Digite o {contador}° valor:'))
    if valor %2 == 0:
        valor_geral[0].append(valor)
    if valor %2 == 1:
        valor_geral[1].append(valor)
valor_geral[0].sort()
valor_geral[1].sort()
print('='*30)
print(f'Os valores pares digitados foram {valor_geral[0]}')
print(f'Os valores ímpares digitados foram {valor_geral[1]}')

    
