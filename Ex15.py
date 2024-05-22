d = int(input('Quantos dias alugado?'))
km = float(input('Quantos km rodados?'))
p = (60 * d) + (0.15 * km)
print('O total a pagar é R${:.2f} reais.'.format(p))
