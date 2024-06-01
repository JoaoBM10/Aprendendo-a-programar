maior = 0
soma = 0
nomevelho = ''
idademaior = 0
for intervalo in range(1,5,1):
    print('-'*5,f'{intervalo}ª PESSOA','-'*5)
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip().upper()
    soma += idade
    media = float(soma / 4)
    if sexo == 'M':
        if intervalo == 1:
            maior = idade
        else:
            if idade > maior:
                maior = idade
                nomevelho = nome
    if sexo == 'F':
        if idade < 20:
            idademaior += 1
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maior} anos e se chama {nomevelho}.')
print(f'Ao todo são {idademaior} mulheres com menos de 20 anos.')
