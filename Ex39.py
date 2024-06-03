from datetime import date

nascimento = int(input('Ano de nascimento:'))
ano = date.today().year
idade = int(ano - nascimento)

print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade , ano))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(nascimento + 18))
else:
    print('Ainda faltam {} para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(nascimento + 18))
