cadastro = dict()
pessoas = list()
soma = media = 0

while True:
    cadastro.clear()
    cadastro["Nome"] = str(input('Nome:')).title().strip()
    cadastro["Sexo"] = ' '
    while cadastro["Sexo"] not in 'MF':
        cadastro["Sexo"] = str(input('Sexo [M/F]:')).upper()[0]
        if cadastro["Sexo"] not in 'MF':
            print('Tente novamente!')
    cadastro["Idade"] = int(input('Idade:'))
    soma += cadastro["Idade"]
    pessoas.append(cadastro.copy())
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
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'A média de idade é de {media:.2f} anos.')
print('As mulheres cadastradas foram ', end = '')
for pessoa in pessoas:
    if pessoa["Sexo"] in 'F':
        print(f'{pessoa["Nome"]} ', end = '')
print()
print('Lista de pessoas que estão acima da média:')
for pessoa in pessoas:
    if pessoa["Idade"] >= media:
        print('    ', end = '')
        for keys, values in pessoa.items():
            print(f'{keys} = {values}. ', end = '')
        print()
print('<< ENCERRADO >>')