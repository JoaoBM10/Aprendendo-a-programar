aluno = dict()

aluno['Nome'] = str(input('Nome do aluno:')).title().strip()
aluno['Média'] = float(input('Média do aluno:'))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif aluno['Média'] >=5:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'

print('='*30)
for keys, valor in aluno.items():
    print(f'  - {keys} do aluno é {valor}')
