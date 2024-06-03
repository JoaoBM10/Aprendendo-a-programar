from datetime import date
atual = date.today().year
contmaior = 0
contmenor = 0
for intervalo in range (1,8,1):
    ano = int(input(f'Em que ano a {intervalo}ª pessoa nasceu?'))
    idade = atual - ano
    if idade >= 18:
        contmaior += 1
    else:
        contmenor += 1
print(f'Ao todo temos {contmaior} maiores de idade.')
print(f'E também temos {contmenor} menores de idade.') 
