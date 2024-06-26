cores = ('\033[m',        # 0 = sem cores
         '\033[0;30;41m', # 1 = vermelho
         '\033[0;30;42m', # 2 = verde
         '\033[0;30;43m', # 3 = amarelo
         '\033[0;30;44m', # 4 = roxo
         '\033[0;30;45m', # 5 = rosa
         '\033[7;30m'     # 6 = branco
         )


def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'  ', 4)
    print(cores[3], end='')
    help(comando)
    print(cores[0], end='')


def titulo(msg, cor = 0):
    tamanho = len(msg) + 4
    print(cores[cor], end='') # Adiciona a cor desejada entre 1 e 6
    print('=' * tamanho)
    print(f'  {msg}')
    print('=' * tamanho)
    print(cores[0], end='') # Limpa a cor escolhida 0


comando = ''
while True:
    titulo('Sistema de ajuda PyHELP  ', 2)
    comando = str(input('Função ou Biblioteca ='))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)