from biblioteca.interface import *
from biblioteca.arquivo import *
from time import sleep

arquivo = 'ProjetoMenudeCadastro.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)
else:
    print('O arquivo já existe!')

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo.
        lerArquivo(arquivo)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome:')).title()
        idade = leiaInt('Idade:')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        #Opção de sair do sistema.
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        #Digitou uma opção errada no menu.
        print('\033[31mErro! Digite uma das opções acima.\033[m')
    sleep(1)
