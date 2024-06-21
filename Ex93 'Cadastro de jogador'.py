jogador = dict()
partidas = list()
jogador["Nome"] = str(input('Nome do jogador:'))
total = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
for contador in range(0, total):
    partidas.append(int(input(f'Quantos gols ele fez na {contador+1}ª partida?')))
jogador["Gols"] = partidas[:]
jogador["Total"] = sum(partidas)

print('=='*30)
print(jogador)
print('=='*30)
for keys, values in jogador.items():
    print(f'O campo {keys} tem o valor {values}.')
print('=='*30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for indice, valor in enumerate(jogador["Gols"]):
    print(f'  => Na partida {indice+1}, fez {valor} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')