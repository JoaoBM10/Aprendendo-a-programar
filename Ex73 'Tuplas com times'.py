tabela_brasileirao = ('FLAMENGO','BAHIA','BOTAFOGO','SÃO PAULO','ATHLETICO',
                      'BRAGANTINO','PALMEIRAS','INTERNACIONAL','CRUZEIRO',
                      'ATLÉTICO-MG','FORTALEZA','JUVENTUDE','GRÊMIO','VASCO'
                      'FLUMINENSE','CRICIÚMA','CORINTHIANS','ATLÉTICO-GO',
                      'VITÓRIA','CUIABÁ')

print(f'Os 5 primeiros são {tabela_brasileirao[0:5]}')
print(f'Os 4 últimos são {tabela_brasileirao[-4:]}')
print(f'Times em ordem alfabética: {sorted(tabela_brasileirao)}')
print(f'Em que posição está o CORINTHINAS? {tabela_brasileirao.index('CORINTHIANS')+1} HAHAHAHAHA')
