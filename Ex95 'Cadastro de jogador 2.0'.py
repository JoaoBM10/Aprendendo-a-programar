jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador["Nome"] = str(input('Nome do jogador:'))
    total = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
    partidas.clear()
    for contador in range(0, total):
        partidas.append(int(input(f'Quantos gols ele fez na {contador+1}ª partida?')))
    jogador["Gols"] = partidas[:]
    jogador["Total"] = sum(partidas)
    time.append(jogador.copy())
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper()[0]
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('Tente novamente!')  
print('=='*30)
print('cod ', end = '')
for elementos in jogador.keys():
    print(f'{elementos:<15}', end = '')
print()
print('=='*30)
for indice, valor in enumerate(time):
    print(f'{indice:>3}', end = '')
    for values in valor.values():
        print(f'-{str(values):<15}', end = '')
    print()
print('=='*30)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999:encerrar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com código {busca}. Tente novamente!')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for indice, gols in enumerate(time[busca]["Gols"]):
            print(f'  No jogo {indice+1} fez {gols} gols.')
    print('=='*30)
