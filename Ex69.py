idade18 = homens = mulher20 = 0

while True:
    print('--'*10)
    print('CADASTRE UMA PESSOA')
    print('--'*10)
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    if idade >= 18:
        idade18 +=1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'Total de pessoal com mais de 18 anos: {idade18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulher20} mulheres com menos de 20 anos.')