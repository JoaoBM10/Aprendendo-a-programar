def ficha(nome='<desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s).')

jogador = str(input('Nome:'))
quantidade_gols = str(input('Quantos gols:'))
if quantidade_gols.isnumeric():
    quantidade_gols = int(quantidade_gols)
else:
    quantidade_gols = 0
if jogador.strip() == '':
    ficha(gols = quantidade_gols)
else:
    ficha(jogador, quantidade_gols)
