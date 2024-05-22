co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
h = (co**2 + ca**2) ** (1/2)
print('O valor da hipotenusa é {:.2f}.'.format(h))

#Outro método

import math

co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
h = math.hypot(co , ca)
print('O valor da hipotenusa é {:.2f}.'.format(h))