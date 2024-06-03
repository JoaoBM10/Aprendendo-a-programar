s = float(input('Digite o salário atual: R$'))
a = s * 0.15
sa = s + a
print('Você recebeu um aumento de 15%, seu salário passa a ser R${}'.format(sa))

#Outro método

s = float(input('Digite o salário atual: R$'))
sa = s + (s * 0.15)
print('Você recebeu um aumento de 15%, seu salário passa a ser R${}'.format(sa))

