v = float(input('Digite o preço do produto: R$'))
d = v * 0.05
vd = v - d
print('O valor com desconto é R${:.2f}'.format(vd))

#Outro método

p = float(input('Digite o preço do produto: R$'))
d = p - ( p * 5 / 100)
print('O valor com desconto é R${:.2f}'.format(d))

