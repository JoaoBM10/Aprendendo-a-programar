lista = list()

while True:
    nome = str(input('Nome do aluno:')).title().strip()
    nota1 = float(input('Primeira nota:'))
    nota2 = float(input('Segunda nota:'))
    media = (nota1 + nota2) /2
    lista.append([nome, [nota1, nota2], media])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('Valor inválido.')
print('=='*13)
print(f'{'No.':<4}{'NOME':<10}{'MEDIA':>12}')
print('='*26)
for indice, aluno in enumerate(lista):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>12.1f}')

while True:
    print('-'*26)
    opcao = str(input('Digite o nome do aluno para saber suas notas:')).title().strip()
    
    encontrado = False
    for aluno in lista:
        if aluno[0] == opcao:
            print(f'Notas de {aluno[0]} são {aluno[1]}')
            encontrado = True
            break
    if not encontrado:
        print('Aluno não encontrado')
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer ver a nota de outro aluno? [S/N]')).upper().strip()[0]
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('Valor inválido.')
print(f'{'VOLTE SEMPRE':-^26}')