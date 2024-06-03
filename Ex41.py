from datetime import date

nasc = int(input('Ano de nascimento:'))
atual = date.today().year
idade = int(atual - nasc)
print('O atleta tem {} anos.'.format(idade))
if idade > 25:
    print('Classificação: MASTER')
elif idade >= 20:
    print('Classificação: SENIOR')
elif idade >= 15:
    print('Classificação: JUNIOR')
elif idade >= 9:
    print('Classificação: INFANTIL')
else:
    print('Classificação: MIRIM')

