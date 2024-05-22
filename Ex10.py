v=float(input('Quantos reais você tem na conta bancaria? R$'))
d=5.10
e=5.56
c=v/d
ce=v/e
print('Você pode comprar: US${:.2f} dólares'.format(c))
print('Você pode comprar: EUR{:.2f} euros'.format(ce))
